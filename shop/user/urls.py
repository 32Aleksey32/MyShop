from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet

app_name = 'user'

router = DefaultRouter()

router.register('', CustomUserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
