from .views import authenticate_user, UserListAPIView, UserCreateAPIView
from django.conf.urls import  url

urlpatterns = [
    url(r'login/', authenticate_user),
    url(r'register/', UserCreateAPIView.as_view()),
    url(r'users/', UserListAPIView.as_view())
]
