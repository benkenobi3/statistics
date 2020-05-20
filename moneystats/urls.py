from .views import diagram_data, category_expenses, CategoryCreateAPIView, CategoryListAPIView
from django.conf.urls import url


urlpatterns = [
    url(r'^diagram/$', diagram_data),
    url(r'categories/list', CategoryListAPIView.as_view()),
    url(r'categories/create/', CategoryCreateAPIView.as_view()),
    url(r'categories/(?P<category_id>.+)/expenses/(?P<date_from>.+)/(?P<date_to>.+)', category_expenses)
]
