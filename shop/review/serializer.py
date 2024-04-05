from product.serializer import ProductSerializer
from rest_framework.serializers import ModelSerializer
from user.serializer import UserSerializer

from .models import Review


class ReviewSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'user', 'product', 'text', 'rating')
