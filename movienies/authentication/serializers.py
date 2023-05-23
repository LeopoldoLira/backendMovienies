from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import UserProfile


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name']

class UserSerializer(UserSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff']