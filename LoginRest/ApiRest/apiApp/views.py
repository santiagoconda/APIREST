from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializer import userSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['POST'])
def registro(request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_RQUEST)
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid pasword'}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = userSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
