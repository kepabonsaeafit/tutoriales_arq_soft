from django.shortcuts import render
from django.views import View

from .infra.factories import PaymentFactory
from .models import Inventario
from .services import CompraService


class CompraView(View):
    """
    CBV: Vista Basada en Clases.
    ActÃºa como un "Portero": recibe la peticiÃ³n y delega al servicio.
    """

    template_name = 'tienda_app/compra.html'

    def setup_service(self):
        gateway = PaymentFactory.get_processor()
        return CompraService(procesador_pago=gateway)

    def get(self, request, libro_id):
        servicio = self.setup_service()
        contexto = servicio.obtener_detalle_producto(libro_id)
        return render(request, self.template_name, contexto)

    def post(self, request, libro_id):
        servicio = self.setup_service()
        try:
            total = servicio.ejecutar_compra(libro_id, cantidad=1)
            return render(
                request,
                self.template_name,
                {
                    'mensaje_exito': f"Â¡Gracias por su compra! Total: ${total}",
                    'total': total,
                },
            )
        except (ValueError, Exception) as e:
            return render(request, self.template_name, {'error': str(e)}, status=400)


class InventarioView(View):
    template_name = 'tienda_app/inventario.html'

    def get(self, request):
        inventario = Inventario.objects.select_related('libro').order_by('libro__titulo')
        return render(request, self.template_name, {'inventario': inventario})
