from tienda_app.infra.factories import PaymentFactory
from tienda_app.services import CompraService
from tienda_app.models import Inventario

servicio = CompraService(procesador_pago=PaymentFactory.get_processor())
inv = Inventario.objects.filter(cantidad__gt=0).select_related("libro").first()
if not inv:
    raise SystemExit("No hay inventario disponible")

servicio.ejecutar_compra(inv.libro.id, cantidad=1)
print("ok")
