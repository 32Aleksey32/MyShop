from cart.views import CartViewSet
from cart_product.views import CartProductViewSet
from category.views import CategoryViewSet
from config.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from order.views import OrderViewSet
from order_product.views import OrderProductViewSet
from product.views import ProductViewSet
from rest_framework.routers import DefaultRouter
from review.views import ReviewViewSet
from user.views import CustomUserViewSet

router = DefaultRouter()

router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'user', CustomUserViewSet)
router.register(r'order', OrderViewSet)
router.register(r'order_product', OrderProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart_product', CartProductViewSet)
router.register(r'review', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('drf-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('category/', include('category.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('order_product/', include('order_product.urls')),
    path('cart/', include('cart.urls')),
    path('cart_product/', include('cart_product.urls')),
    path('review/', include('review.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
