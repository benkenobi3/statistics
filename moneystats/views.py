from datetime import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Category
from .serializers import DiagramCategorySerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def diagram_data(request: Request) -> Response:

    date_from, date_to = request.query_params['date_from'], request.query_params['date_to']
    date_range = (datetime.fromtimestamp(date_from), datetime.fromtimestamp(date_to))

    categories = Category.objects.filter(expenses__user=request.user, expenses__date__range=date_range)
    serialized_objects = DiagramCategorySerializer(instance=categories)

    return Response(serialized_objects)
