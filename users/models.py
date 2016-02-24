from __future__ import unicode_literals


from django.contrib.auth.models import User
from datetime import date
from django.db import models
from scores.models import ResidentialCollege


class AdminUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	isMaster = models.BooleanField(default=False)
	residentialCollege = models.ForeignKey(ResidentialCollege, on_delete=models.CASCADE)
