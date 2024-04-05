from rest_framework import viewsets
from rest_framework.response import Response

from .models import Order
from .serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        """
        Получаем заказы пользователя
        """
        user_id = request.query_params.get('user_id')
        if user_id:
            orders = self.queryset.filter(user_id=user_id).order_by('-date')
        else:
            orders = self.queryset

        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)
