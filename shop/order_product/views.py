from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED

from .models import OrderProduct
from .serializer import OrderProductSerializer


class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def create(self, request, *args, **kwargs):
        # Запрещаем создавать товары в заказе
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
