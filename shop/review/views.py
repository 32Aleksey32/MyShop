from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializer import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # При создании отзыва берем текущего пользователя
        serializer.save(user=self.request.user)
