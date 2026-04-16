from django.urls import path

from .api.views import CompraAPIView, ProductosV1APIView
from .views import CompraView, InventarioView

urlpatterns = [
    path('inventario/', InventarioView.as_view(), name='inventario'),
    path('compra/<int:libro_id>/', CompraView.as_view(), name='finalizar_compra'),
    path('api/v1/productos/', ProductosV1APIView.as_view(), name='api_productos_v1'),
    path('api/v1/comprar/', CompraAPIView.as_view(), name='api_comprar'),
]
