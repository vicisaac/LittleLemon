"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views

# Initialize the DefaultRouter for User API
#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet, basename='user')

# Create a separate router for restaurant-related endpoints (like the tables API)
restaurant_router = routers.DefaultRouter()
restaurant_router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include URLs from the restaurant app (e.g., for menu or other restaurant views)
    path('restaurant/', include('restaurant.urls')),  # Keeps the original restaurant URLs
    
    # Include router-generated URLs for the 'tables' endpoint under restaurant/
    path('restaurant/booking/', include(restaurant_router.urls)),  # Tables API under 'restaurant/'
    
    # Include User-related API under 'api-auth/'
    #path('api-auth/', include(router.urls)),  # Users API under 'api-auth/'
    
    # Include Djoser endpoints for user authentication
    path('auth/', include('djoser.urls')),  # This provides user registration and other related endpoints
    path('auth/', include('djoser.urls.authtoken')),  # This provides token-based authentication

]
