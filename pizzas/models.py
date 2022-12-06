from django.db import models

# Create your models here.

class Pizza(models.Model):# Modèle qui permet de tenir les valeurs des noms
	name = models.CharField(max_length=200) #Field made of characters with a limit 
	date_added = models.DateTimeField(auto_now_add=True)#Field which record
														#date and time
	def __str__(self):#Attribute used by default when there is information about a topic
		"""Return a string representation of the model."""
		return self.name

class Topping(models.Model):
	pizza = models.ForeignKey('Pizza', on_delete = models.CASCADE)#Connect to each entry to a specific topic
	date_added = models.DateTimeField(auto_now_add=True)#Present entries in chronological order
	topping_list = models.TextField() #Field made of characters with a limit 

	class Meta:
		verbose_name_plural = 'Topping List'

	def __str__(self):#Attribute used by default when there is information about a topic
		"""Return a string representation of the model."""
		return self.topping_list

