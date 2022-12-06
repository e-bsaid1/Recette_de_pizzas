"""Defines URL patterns for pizza livrable"""

from django.urls import path

from . import views

app_name = 'recette_pizza'
urlpatterns = [
	# Home page
	path('',views.index, name='index'),
	# Définition de l'URL de la page contenant les noms de pizzas
	path('pizzas/', views.pizzas, name='pizzas'),
	#URL de la page des garnitures de pizzas
	path('pizzas/<int:pizza_id>/',views.pizza, name='pizza'),
]




