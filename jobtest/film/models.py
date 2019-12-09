from django.db import models

# Create your models here.
class Movie(models.Model):
	title	= models.CharField(max_length=200)
	genre	= models.CharField(max_length=200)
	poster	= models.CharField(max_length=200) #todo bedre måde at gøre billedet på med API
	media	= models.CharField(max_length=200)
	def __str__(self):
		return self.title