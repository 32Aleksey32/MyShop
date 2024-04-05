from django.db.models import CharField, Model


class Category(Model):
    name = CharField(unique=True, max_length=100, verbose_name='Наименование')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'shop"."categories'

    def __str__(self):
        return self.name
