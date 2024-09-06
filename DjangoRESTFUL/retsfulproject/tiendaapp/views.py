from warnings import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import Customializer,ProductoSerializer,pedidosSerializer,metodopagoSerializers
from .filters import ProductoFilter

from django.shortcuts import get_object_or_404
from . models import Custom,Producto,pedidos, MetodoPago
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# # Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    pass

class MyTokenRefreshView(TokenRefreshView):
    pass

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user = get_object_or_404(Custom, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = Customializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def register (request):
    serializer = Customializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user  = Custom.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile (request):
    serializer = Customializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def register_product(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'producto': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def register_metodPago(request):
    serializer = metodopagoSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'metodopago': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def register_pedidos(request):
    if isinstance(request.data, list):
        serializer = pedidosSerializer(data=request.data, many=True)
    else:
        serializer = pedidosSerializer(data=request.datas)
    if serializer.is_valid():
        serializer.save()
        return Response({'pedidos': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([AllowAny])
def lista_user(request):
    custom = Custom.objects.all()
    serializer = Customializer(custom, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([AllowAny])
def lista_productos(request):
    producto = Producto.objects.all()
    serializer = ProductoSerializer(producto, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def filtrar_productos(request):
    producto_filter = ProductoFilter(request.GET, queryset=Producto.objects.all())
    serializer = ProductoSerializer(producto_filter.qs, many=True)
    return Response (serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def lista_pedidos(request):
    Pedidos = pedidos.objects.all()
    serializer = pedidosSerializer(Pedidos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view (['GET'])
@permission_classes([AllowAny])
def lista_metodopago(request):
    metodo_pago = MetodoPago.objects.all()
    serializer = metodopagoSerializers(metodo_pago, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def actualizar_producto(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductoSerializer(producto, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'producto': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def actualizar_Usuario(request, pk):
    try:
        custom = Custom.objects.get(pk=pk)
    except Custom.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    serializer = Customializer(custom, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'custom': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def eliminar_producto(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    producto.delete()
    return Response({'message': 'Producto eliminado'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def eliminar_usuarios(request,pk):
    try:
        custom = Custom.objects.get(pk=pk)
    except Custom.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    custom.delete()
    return Response({'message': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def eliminar_pedidos(request,pk):
    try:
        pedido = pedidos.objects.get(pk=pk)
    except Custom.DoesNotExist:
        return Response({'error': 'pedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    pedido.delete()
    return Response({'message': 'pedido eliminado'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def eliminar_pagos(request,pk):
    try:
        pagos =MetodoPago .objects.get(pk=pk)
    except MetodoPago.DoesNotExist:
        return Response({'error': 'pago no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    pagos.delete()
    return Response({'message': 'pago eliminado'}, status=status.HTTP_204_NO_CONTENT)