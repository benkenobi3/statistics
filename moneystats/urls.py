from .views import diagram_data
from django.conf.urls import url


urlpatterns = [
    url(r'diagram/<datetime:date_from>&<datetime:date_to>', diagram_data),
]
