from django.db import models
from django.db.models import CASCADE, ForeignKey, Model, PositiveIntegerField
from order.models import Order
from product.models import Product


class OrderProduct(Model):
    order = ForeignKey(Order, on_delete=CASCADE, verbose_name='Заказ')
    product = ForeignKey(Product, on_delete=CASCADE, verbose_name='Товар')
    quantity = PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
        db_table = 'shop"."order_product'

    @property
    def total_price(self):
        return self.price * self.quantity
