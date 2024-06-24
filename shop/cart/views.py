from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED

from .models import Cart
from .serializer import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        # Запрещаем создавать новую корзину
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
