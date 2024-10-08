from rest_framework import viewsets
from rest_framework import mixins
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import OrderProduct
from .serializer import OrderProductSerializer


class OrderProductViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
