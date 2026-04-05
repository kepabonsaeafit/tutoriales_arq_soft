from tienda_app.infra.factories import PaymentFactory
from tienda_app.services import CompraService
from tienda_app.models import Inventario

servicio = CompraService(procesador_pago=PaymentFactory.get_processor())

inv_items = list(Inventario.objects.select_related("libro").filter(cantidad__gt=0)[:3])
if len(inv_items) < 3:
    raise SystemExit("Se requieren al menos 3 libros con stock para la prueba")

for inv in inv_items:
    total = servicio.ejecutar_compra(inv.libro.id, cantidad=1)
    print(f"compra_ok:{inv.libro.titulo}:{total}")
