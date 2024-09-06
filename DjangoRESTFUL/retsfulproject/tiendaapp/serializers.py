from rest_framework import serializers
# from django.contrib.auth.models import Custom
from . models import Custom, Producto, pedidos,MetodoPago,Cart


class Customializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = ('id','imagen','first_name','username','email','password','is_staff')
        extra_kwargs = {
            'is_staff': {'read_only': False}, 
        }
        

        def create(self, validated_data):
            user = Custom.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password']
            )
            if 'is_staff' in validated_data:
                user.is_staff = validated_data['is_staff']
                user.save()
            return user
            

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields ='__all__'

class pedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedidos
        fields ='__all__'
class metodopagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields ='__all__'

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields ='__all__'

