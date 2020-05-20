from datetime import datetime

from django.db.models import Sum, F, Value, CharField
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def diagram_data(request: Request) -> Response:

    date_from, date_to = int(request.query_params['date_from']), int(request.query_params['date_to'])
    date_range = (datetime.fromtimestamp(date_from), datetime.fromtimestamp(date_to))

    category_total = Category.objects.values('name')\
        .filter(expenses__user=request.user, expenses__date__range=date_range)\
        .annotate(category_id=F('id'), total=Sum('expenses__price'))

    return Response(category_total)


class CategoryCreateAPIView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    model = Category
    serializer_class = CategorySerializer


class CategoryListAPIView(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
