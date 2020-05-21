from .views import authenticate_user, UserCreateAPIView
from django.conf.urls import url


urlpatterns = [
    url(r'^login/$', authenticate_user),
    url(r'register/', UserCreateAPIView.as_view()),
]
