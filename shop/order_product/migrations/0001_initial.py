# Generated by Django 4.2.6 on 2024-04-11 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_alter_order_options_rename_date_order_created_at_and_more'),
        ('product', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
                'db_table': 'shop"."order_product',
            },
        ),
    ]
