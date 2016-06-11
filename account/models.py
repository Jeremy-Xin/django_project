from django.db import models


# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=10)
	user_email = models.CharField(max_length=30)
	user_age = models.IntegerField()
