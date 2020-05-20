from .views import diagram_data, CategoryCreateAPIView, CategoryListAPIView
from django.conf.urls import url


urlpatterns = [
    url(r'^diagram/$', diagram_data),
    url(r'categories/create/', CategoryCreateAPIView.as_view()),
    url(r'categories/list', CategoryListAPIView.as_view())
]
