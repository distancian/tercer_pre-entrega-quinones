
from django.urls import path
from wine_app.views import cliente, buscar, busquedaProducto, vendedor, producto, listar_clientes, listar_productos, listar_vendedores, inicio, agregar_producto, agregar_cliente, agregar_vendedor

urlpatterns = [
    path('agrega-cliente/<nombre>/<apellido>/<dni>/<mail>', cliente),
    path('agrega-producto/<bodega>/<etiqueta>/<precio>', producto),
    path('agrega-vendedor/<nombre>/<apellido>/<legajo>', vendedor),
    path('listar_clientes', listar_clientes, name='listar_clientes'),
    path('listar_productos', listar_productos, name='listar_productos'),
    path('listar_vendedores', listar_vendedores, name='listar_vendedores'),
    path('agregar_producto', agregar_producto, name='agregar_producto'),
    path('agregar_cliente', agregar_cliente, name='agregar_cliente'),
    path('agregar_vendedor', agregar_vendedor, name='agregar_vendedor'),
    path('busquedaProducto', busquedaProducto, name='busquedaProducto'),
    path('buscar', buscar, name='buscar'),
    path('inicio', inicio, name='inicio'),

]
