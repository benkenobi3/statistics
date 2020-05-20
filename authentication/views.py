from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_jwt.settings import api_settings

from .serializers import UserCreateSerializer


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


@api_view(['POST'])
def authenticate_user(request):

    username = request.data.get('username')
    password = request.data.get('password')

    if bool(username) & bool(password):

        user = User.objects.get(username=username)

        if user:

            if user.check_password(password):
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                res = {
                    'token': token
                }
                return Response(res, status=status.HTTP_200_OK)
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'
                }
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        else:
            res = {
                'error': 'con not find user with specified username'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    else:
        res = {
            'error': 'please provide a username and a password'
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class UserCreateAPIView(generics.CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
