from django.contrib import admin

from .models import OrderProduct

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'total_price')
    # list_filter = ('cart', 'product',)
    search_fields = ('order__id', 'product__name',)