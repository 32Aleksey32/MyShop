
from django.db.models import CASCADE, CharField, ForeignKey, ImageField, IntegerField, Model


class Product(Model):
    name = CharField(unique=True, max_length=100, verbose_name='Наименование')
    price = IntegerField(default=0, verbose_name='Цена')
    description = CharField(max_length=250, default='', blank=True, null=True, verbose_name='Описание')
    category = ForeignKey('category.Category', on_delete=CASCADE, related_name='products', verbose_name='Категория')
    image = ImageField(upload_to='product_images/', verbose_name='Изображение')

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'shop"."products'

    def __str__(self):
        return f'{self.name} ({self.price} руб.)'
