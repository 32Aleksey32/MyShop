from cart.models import Cart
from django.db.models import CASCADE, ForeignKey, Model, PositiveIntegerField
from product.models import Product


class CartProduct(Model):
    cart = ForeignKey(Cart, on_delete=CASCADE, related_name='products', verbose_name='Корзина')
    product = ForeignKey(Product, on_delete=CASCADE, verbose_name='Товар')
    quantity = PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
        db_table = 'shop"."cart_product'


    def __str__(self):
        return f'{self.product} в корзине № {self.cart.id}'

    @property
    def total_price(self):
        return self.quantity * self.product.price
