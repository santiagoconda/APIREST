from django_filters import rest_framework as filters
from .models import Producto
class ProductoFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    precio = filters.NumberFilter(lookup_expr='icontains')

    class Meta:
        model = Producto
        fields = ['nombre', 'precio']