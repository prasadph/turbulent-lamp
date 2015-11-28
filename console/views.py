# from django.shortcuts import render
from .models import Food
from rest_framework import viewsets
from .serializers import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):

    """docstring for FoodViewSet"""

    queryset = Food.objects.all().order_by('pk')
    serializer_class = FoodSerializer
