from django.db import models

class Videogame(models.Model):
	title = models.CharField(max_length = 200)
	year = models.DateTimeField('date released')
	rating = models.IntegerField(default = 0)
	beaten = models.BooleanField(default = False)
	publisher = models.CharField(max_length = 200)
	description = models.CharField(max_length = 500)
