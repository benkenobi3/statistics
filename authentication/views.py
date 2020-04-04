from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .serializers import UserSerializer, UserCreateSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):

    model = User
    serializer_class = UserCreateSerializer

    permission_classes = [
        permissions.AllowAny
    ]
