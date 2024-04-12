from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, DateTimeField, ForeignKey, IntegerField, Model, TextField
from product.models import Product
from user.models import User


class Review(Model):
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='Пользователь')
    product = ForeignKey(Product, on_delete=CASCADE, verbose_name='Товар')
    text = TextField(blank=True, default='', verbose_name='Текст')
    rating = IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Рейтинг')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        db_table = 'shop"."reviews'

    def __str__(self):
        return f'{self.product}, {self.user}'
