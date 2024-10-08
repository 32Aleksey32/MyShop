from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Cart
from .serializer import CartSerializer


class CartViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
