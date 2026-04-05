from tienda_app.models import Libro, Inventario
for inv in Inventario.objects.select_related("libro"):
    print(inv.libro.titulo, inv.cantidad)
