from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CartProductViewSet

app_name = 'cart_product'

router = DefaultRouter()

router.register('', CartProductViewSet, basename='cart_product')


urlpatterns = [
    path('', include(router.urls)),
]
