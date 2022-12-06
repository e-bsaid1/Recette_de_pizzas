"""Prend les données liés aux noms de pizzas et garnitures pour générer une page et les renvoie au navigateur"""

from django.shortcuts import render
from .models import Pizza, Topping #import du modèle Pizza

# Create your views here.
def index(request): 
	"""The home page for Pizza livrable."""
	return render(request, 'pizzas/index.html')

def pizzas(request):
	"""Show all pizzas names."""
	pizzas = Pizza.objects.order_by('?')#demande des objets Pizzas et triage chronologique
	context = {'pizzas': pizzas}#accès aux noms de pizzas et envoi vers le template
	return render(request, 'pizzas/pizzas.html', context)#envoie des noms de pizzas vers le template

def pizza(request, pizza_id):
	"""Montre le nom de la pizza et tout sa garniture."""
	pizza = Pizza.objects.get(id=pizza_id)#Reprend le nom de pizza
	toppings = pizza.topping_set.order_by('-date_added')
	context = {'pizza': pizza, 'toppings':toppings}
	return render(request, 'pizzas/pizza.html', context)


