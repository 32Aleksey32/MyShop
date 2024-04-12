from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from .models import Order


class OrderSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'address', 'created_at', 'status')
