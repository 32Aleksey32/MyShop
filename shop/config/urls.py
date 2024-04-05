from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('drf-auth/', include('rest_framework.urls')), # login/ или logout/

    # чтобы получить токен, заходим на token/ и отправляем username/пароль и получаем access токен,
    # его используем в headers: Bearer и сам токен
    # если прошло 5 мин и токен недействительный то берем refresh токен и отправляем его на ссылку ниже
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('category/', include('category.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('cart/', include('cart.urls')),
    path('cart_product/', include('cart_product.urls')),
    path('review/', include('review.urls')),
]
