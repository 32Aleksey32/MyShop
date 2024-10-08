from django.contrib import admin

from .models import CartProduct


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price')
    search_fields = ('cart__user__username', 'product__name',)
