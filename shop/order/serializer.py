from cart.models import Cart
from order_product.models import OrderProduct
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Order


class OrderSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'address', 'created_at', 'status')
        read_only_fields = ('status',)

    def create(self, validated_data):
        """Создает заказ из товаров в корзине пользователя и очищает корзину."""
        user = self.context['request'].user
        cart = Cart.objects.get(user=user)

        # Проверяем, есть ли товары в корзине
        if not cart.products.exists():
            raise ValidationError("Не удается создать заказ из пустой корзины")

        order = Order.objects.create(
            user=user,
            status='NEW',
            address=validated_data['address']
        )

        for cart_product in cart.products.all():
            OrderProduct.objects.create(
                order=order,
                product=cart_product.product,
                quantity=cart_product.quantity,
                price=cart_product.product.price
            )

        cart.products.all().delete()
        return order
