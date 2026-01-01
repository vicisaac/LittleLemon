# restaurant/models.py
from django.db import models

# Booking model
class Booking(models.Model):
    # Fields
    name = models.CharField(max_length=255)  # Name of the person booking
    no_of_guests = models.IntegerField()     # Number of guests for the booking
    booking_date = models.DateTimeField()    # Date and time of the booking

    # Meta information (optional, can help in defining DB constraints)
    class Meta:
        db_table = 'booking'  # The table name in the database (Django defaults to using the model's name)

    # String representation of the object
    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"

# Menu model
class Menu(models.Model):
    # Fields
    title = models.CharField(max_length=355)  # Name or title of the menu item
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the menu item
    inventory = models.IntegerField()  # Quantity in stock of the menu item

    # Meta information (optional, can help in defining DB constraints)
    class Meta:
        db_table = 'menu'  # The table name in the database (Django defaults to using the model's name)

    # String representation of the object
    def __str__(self):
        return f"{self.title} - ${self.price}"
