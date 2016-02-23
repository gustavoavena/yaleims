from __future__ import unicode_literals


from django.contrib.auth.models import User
from datetime import date
from django.db import models


# Create your models here.


SPORTS = ("men_socer", "women_soccer", "men_footbal", "women_footbal")

COLLEGES_CHOICES = (
	('BK', 'Berkeley College'),
	('BR', 'Branford College'),
	('CC', 'Calhoun College'),
	('DC', 'Davenport College'),
	('ES', 'Ezra Stile College'),
	('JE', 'Jonathan Edwards College'),
	('MC', 'Morse College'),
	('PC', 'Pierson College'),
	('SM', 'Silliman College'),
	('SY', 'Saybrook College'),
	('TC', 'Trumbull College'),
	('TD', 'Timothy Dwight College'),
)



#the stats tabl
class ResidentialCollege(models.Model): 
	name = models.CharField(max_length=2, choices=COLLEGES_CHOICES, unique=True)
	img_URL = models.CharField(max_length=1024)
	total = models.IntegerField()
	description = models.TextField(default='')

class Sport(models.Model):
	sport = models.CharField(max_length=30)



class Match(models.Model):
	sport = models.ForeignKey(Sport, related_name="matches")
	date = models.DateField(default=date.today())
	colleges = models.ManyToManyField(ResidentialCollege, related_name="matches", through="Points")

class Points(models.Model):
	college = models.ForeignKey(ResidentialCollege, on_delete=models.CASCADE)
	match = models.ForeignKey(Match, on_delete=models.CASCADE)
	points = models.IntegerField()


# Calhoun = ResidentialCollege(
# 	name = 'CC',
# 	img_URL = '',
# 	total = 0

# )
