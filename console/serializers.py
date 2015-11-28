from rest_framework import serializers
from .models import Food, Customer


class FoodSerializer(serializers.HyperlinkedModelSerializer):

    """docstring for FoodSerializer"""

    class Meta:
        model = Food
        fields = ('name', 'cost')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    """docstring for CustomerSerializer"""

    class Meta:
        model = Customer
