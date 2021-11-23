from django.contrib import admin
from .models import Links, Videos, Image
# Register your models here.

class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'github', 'linkdin')
    list_display_links = ('id', 'github')

class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    
admin.site.register(Links, LinksAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(Image, ImageAdmin)




