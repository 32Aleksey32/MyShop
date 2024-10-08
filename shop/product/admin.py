from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'price', 'category__name')