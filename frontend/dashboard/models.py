from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
	# first_name = models.CharField()
	# last_name = models.CharField()
    political_score = models.IntegerField()
    dob = models.DateField()