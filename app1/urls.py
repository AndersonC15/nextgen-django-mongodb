from django.urls import path
from . import views

urlpatterns = [
    # INICIO / DASHBOARD
    path('', views.inicio, name='inicio'),

    # PRODUCTOS
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    # EMPLEADOS
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleados/editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),

    # MARCAS
    path('marcas/', views.lista_marcas, name='lista_marcas'),
    path('marcas/crear/', views.crear_marca, name='crear_marca'),
    path('marcas/eliminar/<int:id>/', views.eliminar_marca, name='eliminar_marca'),

    # SUCURSALES
    path('sucursales/', views.lista_sucursales, name='lista_sucursales'),
    path('sucursales/crear/', views.crear_sucursal, name='crear_sucursal'),
    path('sucursales/editar/<int:id>/', views.editar_sucursal, name='editar_sucursal'), # <--- Esta es la que arregla el error
    path('sucursales/eliminar/<int:id>/', views.eliminar_sucursal, name='eliminar_sucursal'),

    # PEDIDOS
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/crear/', views.crear_pedido, name='crear_pedido'),
    path('pedidos/eliminar/<int:id>/', views.eliminar_pedido, name='eliminar_pedido'),
]