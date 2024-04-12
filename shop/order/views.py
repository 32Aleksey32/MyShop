from rest_framework import viewsets
from .models import Order
from .serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # При создании заказа берем текущего пользователя
        serializer.save(user=self.request.user)
