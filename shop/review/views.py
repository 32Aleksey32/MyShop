from rest_framework import viewsets
from rest_framework.response import Response

from .models import Review
from .serializer import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        """
        Получаем отзывы покупателя
        """
        user_id = request.query_params.get('user_id')
        if user_id:
            reviews = self.queryset.filter(user_id=user_id)
        else:
            reviews = self.queryset

        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)
