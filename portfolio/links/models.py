from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Links(models.Model):
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkdin = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    