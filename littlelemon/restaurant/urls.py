#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

# The index() view renders the 'index.html' template when the root URL is accessed.