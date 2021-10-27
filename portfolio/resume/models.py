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
    

