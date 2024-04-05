from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ReviewViewSet

app_name = 'review'

router = DefaultRouter()

router.register('', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),
]
