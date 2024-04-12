from rest_framework.relations import PrimaryKeyRelatedField, StringRelatedField

from rest_framework.serializers import ModelSerializer

from .models import Review


class ReviewSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)
    product = StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'user', 'product', 'text', 'rating')
