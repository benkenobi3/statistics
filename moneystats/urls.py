from .views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^diagram/$', diagram_data),
    url(r'expenses/list', ExpenseListAPIView.as_view()),
    url(r'expenses/create', ExpenseCreateAPIView.as_view()),
    url(r'categories/list', CategoryListAPIView.as_view()),
    url(r'categories/create/', CategoryCreateAPIView.as_view()),
    url(r'categories/(?P<category_id>.+)/expenses/', category_expenses)
]
