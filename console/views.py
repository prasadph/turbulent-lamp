# from django.shortcuts import render
from .models import Food, Customer, Order
from rest_framework import viewsets
from .serializers import FoodSerializer, CustomerSerializer, OrderSerializer


class FoodViewSet(viewsets.ModelViewSet):

    """docstring for FoodViewSet"""

    queryset = Food.objects.all().order_by('pk')
    serializer_class = FoodSerializer


class CustomerViewSet(viewsets.ModelViewSet):

    """docstring for CustomerViewSet"""

    queryset = Customer.objects.all().order_by('pk')
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):

    """docstring for OrderViewSet"""

    queryset = Order.objects.all().order_by('pk')
    serializer_class = OrderSerializer
