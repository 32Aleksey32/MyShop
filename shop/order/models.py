from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, IntegerField, Model
from product.models import Product
from user.models import User

status_choices = [
    ('NEW', 'Новый'),
    ('PROCESSING', 'В обработке'),
    ('SHIPPED', 'Отправлен'),
    ('DELIVERED', 'Доставлен'),
    ('CANCELLED', 'Отменен'),
    ('RETURN', 'Возврат'),
]


class Order(Model):
    product = ForeignKey(Product, on_delete=CASCADE, verbose_name='Товар')
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='Пользователь')
    quantity = IntegerField(default=1, verbose_name='Количество')
    address = CharField(max_length=50, default='', blank=True, verbose_name='Адрес')
    date = DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    status = CharField(choices=status_choices)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'shop"."orders'

    def __str__(self):
        return f'{self.product}, {self.user}'

    @property
    def price(self):
        return self.quantity * self.product.price

    @property
    def phone_number(self):
        return self.user.phone_number
