from .serializers import  ProductoSerializer
from rest_framework import viewsets, permissions
from .models import Producto, Pedidios


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


