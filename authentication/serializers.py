from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return Response(user, status=status.HTTP_201_CREATED)

    class Meta:
        model = User
        fields = '__all__'
