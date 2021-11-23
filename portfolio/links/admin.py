from django.contrib import admin
from .models import Links, Videos
# Register your models here.

class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'github', 'linkdin')
    list_display_links = ('id', 'github')

class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    
admin.site.register(Links, LinksAdmin)
admin.site.register(Videos, VideosAdmin)



