from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Food, FoodCategory
from .serializers import FoodSerializer, FoodListSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """API endpoint, позволяющий просматривать или редактировать еду"""
    queryset = Food.objects.filter(is_publish=True).order_by('id')
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]


class FoodListViewSet(APIView):
    """API endpoint, позволяющий просматривать или редактировать список еды"""
    def get(self, request):
        foodcategory = FoodCategory.objects.filter(food__is_publish=True).order_by('id').distinct()
        serializer = FoodListSerializer(foodcategory, many=True)
        return Response(serializer.data)
