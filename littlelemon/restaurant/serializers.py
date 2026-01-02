
# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking  # Import the Menu and Booking models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']  # Specify the fields to serialize


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Include all fields of the Booking model
        #fields = ['id', 'name', 'date', 'time', 'guests']  # Specify the fields to serialize