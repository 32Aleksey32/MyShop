from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'text', 'score', 'created_at')
    list_filter = ('score', 'created_at')
    search_fields = ('user', 'product__name', 'rating')
