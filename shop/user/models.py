from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField


class User(AbstractUser):
    last_name = CharField(verbose_name='Фамилия')
    first_name = CharField(verbose_name='Имя')
    middle_name = CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    phone_number = CharField(max_length=12, verbose_name='Номер мобильного телефона')
    email = EmailField(verbose_name='Электронная почта')
    password = CharField(verbose_name='Пароль')

    class Meta:
        ordering = ['last_name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'shop"."users'

    def __str__(self):
        return self.username
