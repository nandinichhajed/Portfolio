from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    score = models.IntegerField(default=50, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills')
    is_key_skill = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(blank=True, null=True, max_length=100)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class ContactProfile(models.Model):
    
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    def __str__(self):
        return f'{self.name}'
    
