from rest_framework import mixins, viewsets

from .models import OrderProduct
from .serializer import OrderProductSerializer


class OrderProductViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
