from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
from .models import Menu, Booking
from .serializers import UserSerializer, MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# UserViewSet handles CRUD operations for the User model
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Queryset to retrieve all users
    serializer_class = UserSerializer  # Serializer to use for User model
    
# MenuViewSet handles CRUD operations for the Menu model
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()  # Get all Menu items
    serializer_class = MenuSerializer  # Use the MenuSerializer for serialization  
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Get all Menu items
    serializer_class = MenuSerializer  # Use the MenuSerializer for serialization
    lookup_field = 'id'  # Specify that the lookup is by 'id'

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Queryset to retrieve all bookings
    serializer_class = BookingSerializer  # Serializer to use for Booking model