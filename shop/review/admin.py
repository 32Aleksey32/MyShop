from django.contrib import admin

from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'text', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user', 'product__name', 'rating')