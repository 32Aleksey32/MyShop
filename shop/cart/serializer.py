from cart_product.serializer import CartProductSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from user.serializer import UserSerializer

from .models import Cart


class CartSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    products = CartProductSerializer(many=True, read_only=True)
    total_price_an_cart = SerializerMethodField()

    def get_total_price_an_cart(self, obj):
        total_price_an_cart = 0
        for product in obj.products.all():
            total_price_an_cart += product.total_price
        return total_price_an_cart

    class Meta:
        model = Cart
        fields = ('id', 'user', 'products', 'created_at', 'updated_at', 'total_price_an_cart')
