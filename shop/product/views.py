from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        """
        Получаем товары по категории
        """
        #  /product/?category_id=1
        category_id = request.query_params.get('category_id')
        if category_id:
            products = self.queryset.filter(category_id=category_id)
        else:
            products = self.queryset

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
