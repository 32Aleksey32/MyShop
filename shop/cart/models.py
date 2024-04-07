from django.db.models import CASCADE, DateTimeField, Model, OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User


class Cart(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='cart', verbose_name='Пользователь')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        db_table = 'shop"."cart'

    def __str__(self):
        return f'Корзина пользователя {self.user.username}'


@receiver(post_save, sender=User)
def create_order(sender, instance, created, **kwargs):
    """При создании нового пользователя создается объект Cart"""
    if created:
        Cart.objects.create(user=instance, id=instance.id)
