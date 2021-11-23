from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Links(models.Model):
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkdin = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    github = models.CharField(max_length=200)

class Videos(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    video = models.FileField(upload_to='media', blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        
    def __str__(self):
        return self.title
    
class Image(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, )
    image = models.ImageField(upload_to="media", blank=True, null=True)
    
    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
    
    def __str__(self):
        return self.name
