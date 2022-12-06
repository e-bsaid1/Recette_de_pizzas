from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping

Pizza_obj = admin.site.register(Pizza)
Toppings_obj = admin.site.register(Topping)
 