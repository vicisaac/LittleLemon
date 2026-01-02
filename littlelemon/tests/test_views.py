# tests/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few Menu items for testing
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=60, inventory=200)

        # Initialize the API client
        self.client = APIClient()

    def test_get_all_items(self):
        # Get the list of Menu items via the API
        #url = reverse('menuitem-list')  # Assuming the name of the URL pattern is 'menuitem-list'
        url = reverse('menu_list_create')  # Adjusted to match the view name
        response = self.client.get(url)

        # Assert that the response status is OK (200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response data matches the created items
        self.assertEqual(len(response.data), 2)  # There should be 2 items in the list
        self.assertEqual(response.data[0]['title'], "Pizza")
        self.assertEqual(response.data[1]['title'], "Burger")
