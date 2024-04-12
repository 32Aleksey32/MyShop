from django.db import transaction
from order.models import Order
from order_product.models import OrderProduct
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_405_METHOD_NOT_ALLOWED

from .models import Cart
from .serializer import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        # Запрещаем создавать новую корзину
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)

    def get_queryset(self):
        # Убеждаемся, что пользователь видит только свою корзину
        return self.queryset.filter(user=self.request.user)

    @action(detail=True, methods=['post'], url_path='create-order')
    @transaction.atomic
    def create_order(self, request, pk=None):
        """Создает заказ из товаров в корзине пользователя и очищает корзину."""
        cart = Cart.objects.get(user=request.user)
        # Проверяем, есть ли товары в корзине
        if not cart.products.exists():
            return Response({"error": "Не удается создать заказ из пустой корзины"}, status=HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=request.user, status='NEW')

        for cart_product in cart.products.all():
            OrderProduct.objects.create(
                order=order,
                product=cart_product.product,
                quantity=cart_product.quantity,
                price=cart_product.product.price
            )

        cart.products.all().delete()
        return Response({"message": "Заказ успешно создан"}, status=HTTP_201_CREATED)
