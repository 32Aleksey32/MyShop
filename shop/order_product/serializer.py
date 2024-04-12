from order.serializer import OrderSerializer
from rest_framework.serializers import ModelSerializer

from .models import OrderProduct


class OrderProductSerializer(ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ('id', 'order', 'product', 'quantity', 'price', 'total_price')
        read_only_fields = ('product', 'quantity', 'price')
