from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .api import ProductoViewSet
from . import views


# router = DefaultRouter()
# router.register('api/producto', ProductoViewSet, 'producto')


urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('profile/',views.profile),
    path('producto/', views.register_product, name='register_product'),
    path('pedidos/',views.register_pedidos, name='register_pedidios'),
    path('lista/productos/',views.lista_productos, name='lista_productos'),
    path('lista/pedidos/',views.lista_pedidos, name='lista_pedidios'),
    path('lista/pagos/', views.lista_metodopago, name="lista_metodoPago"),
    path('productos/<int:pk>/',views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/usuario/<int:pk>/', views.eliminar_usuarios, name="eliminar_usuarios"),
    path('productos/<int:pk>/eliminar/',views.eliminar_producto, name='eliminar_producto'),
    path ('metodopago/',views.register_metodPago, name='register_metopago'),
    path('usuarios/', views.lista_user, name='lista_user'),
    path('actualizar/usuarios/<int:pk>/', views.actualizar_Usuario, name="actualizar_Usuario"),
    path('eliminar/pedidos/<int:pk>/', views.eliminar_pedidos, name="eliminar_pedidos"),
    path('eliminar/pagos/<int:pk>/', views.eliminar_pagos, name="eliminar_pagos"),
    path('filtrar/', views.filtrar_productos, name="filtrar_productos")
] 