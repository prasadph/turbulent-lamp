from rest_framework import serializers
from .models import Food, Customer, Order


class FoodSerializer(serializers.HyperlinkedModelSerializer):

    """docstring for FoodSerializer"""

    class Meta:
        model = Food
        fields = ('name', 'cost', 'description')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    """docstring for CustomerSerializer"""

    class Meta:
        model = Customer
        fields = ('name', 'sex', 'created')


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    """docstring for OrderSerializer"""

    class Meta:
        model = Order
        fields = ('amount', 'address', 'created')
