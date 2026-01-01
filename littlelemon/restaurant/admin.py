from django.contrib import admin
from .models import Booking, Menu

# Register models with the admin interface
admin.site.register(Booking)
admin.site.register(Menu)