from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .models import Food, FoodCategory
from .serializers import FoodSerializer, FoodListSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """API endpoint, позволяющий просматривать или редактировать еду"""
    queryset = Food.objects.filter(is_publish=True).order_by('id')
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]


class FoodListViewSet(viewsets.ModelViewSet):
    """API endpoint, позволяющий просматривать или редактировать список еды"""
    queryset = FoodCategory.objects.filter(food__is_publish=True).order_by('id').distinct()
    serializer_class = FoodListSerializer
    permission_classes = [permissions.IsAuthenticated]