from rest_framework.serializers import ModelSerializer

from .models import CartProduct


class CartProductSerializer(ModelSerializer):

    class Meta:
        model = CartProduct
        fields = ('id', 'product', 'quantity', 'total_price')
