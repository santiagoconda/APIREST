from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom(AbstractUser):
    rol = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

    # def __str__(self) -> str:
    #     return self.username

class Producto(models.Model):
    imagen = models.ImageField(upload_to='images/')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Pedidios(models.Model):
    producto = models.CharField(max_length=10)
    cliente = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)
    nuip = models.IntegerField()
    cardNumber = models.IntegerField()
    cardExpiration = models.DateField()
    cardCVV = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

class Cart(models.Model):
    user = models.OneToOneField(Custom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class pedidos(models.Model):
    nombre = models.CharField(max_length=50,null=True, blank=True)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
