from __future__ import unicode_literals

from django.db import models



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
