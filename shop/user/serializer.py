from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import User


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'first_name', 'middle_name', 'phone_number', 'email', 'password')

    def validate_email(self, data):
        if User.objects.filter(email=data).exists():
            raise ValidationError('Покупатель с таким адресом эл. почты уже существует.')
        return data

    def validate_username(self, data):
        if User.objects.filter(username=data).exists():
            raise ValidationError("Пользователь с таким юзернеймом уже существует.")
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'middle_name', 'phone_number')
