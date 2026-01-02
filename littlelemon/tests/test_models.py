# tests/test_models.py

from django.test import TestCase
from restaurant.models import Menu  # Import the Menu model

class MenuTest(TestCase):
    def test_get_item(self):
        # Create a new Menu item
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)

        # Assert that the string representation matches the expected format
        self.assertEqual(str(item), "IceCream : 80")

