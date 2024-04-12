from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, Model
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
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='Пользователь')
    address = CharField(max_length=50, default='', blank=True, verbose_name='Адрес')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    status = CharField(choices=status_choices)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'shop"."orders'

    def __str__(self):
        return f'Заказ № {self.id}'

    @property
    def price(self):
        return self.quantity * self.product.price
