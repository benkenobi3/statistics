from .views import *
from django.conf.urls import url, include
from rest_framework import routers


urlpatterns = [
    url(r'^diagram/$', diagram_data),
    url(r'expenses/all', ExpenseListAPIView.as_view()),
    url(r'expenses/list', ExpensesUserListAPIVIew.as_view()),
    url(r'expenses/create', ExpenseCreateAPIView.as_view()),
    url(r'^expenses/detail/{pk}/$', ExpenseDetailAPIView.as_view()),
    url(r'categories/list', CategoryListAPIView.as_view()),
    url(r'categories/create/', CategoryCreateAPIView.as_view()),
    url(r'categories/(?P<category_id>.+)/expenses/', category_expenses)
]
