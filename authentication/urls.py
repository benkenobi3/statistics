from .views import UserListAPIView, UserCreateAPIView
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'login/', obtain_jwt_token),
    url(r'register/', UserCreateAPIView.as_view()),
    url(r'users/', UserListAPIView.as_view())
]
