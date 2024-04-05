from product.serializer import ProductSerializer
from rest_framework.serializers import ModelSerializer
from user.serializer import UserSerializer

from .models import Order


class OrderSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'product', 'user', 'quantity', 'price', 'address', 'phone_number', 'date', 'status')
