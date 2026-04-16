from tienda_app.models import Libro, Inventario
items = [
    ("Clean Code en Python", 150.0, 10),
    ("Arquitectura Limpia", 200.0, 10),
    ("Refactoring", 180.0, 10),
]
for titulo, precio, cantidad in items:
    libro, _ = Libro.objects.get_or_create(titulo=titulo, defaults={"precio": precio})
    if float(libro.precio) != float(precio):
        libro.precio = precio
        libro.save()
    Inventario.objects.update_or_create(libro=libro, defaults={"cantidad": cantidad})
print("ok")
