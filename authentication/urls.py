from .views import UserListAPIView
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'login/', obtain_jwt_token),
    url(r'users/', UserListAPIView.as_view()),
]
