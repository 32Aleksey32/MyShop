from djoser.views import UserViewSet

from .models import User
from .serializer import UserCreateSerializer


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
