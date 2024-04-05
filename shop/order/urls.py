from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet

app_name = 'order'

router = DefaultRouter()

router.register('', OrderViewSet, basename='order')


urlpatterns = [
    path('', include(router.urls)),
]
