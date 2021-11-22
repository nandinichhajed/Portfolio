from django.contrib import admin
from .models import Links
# Register your models here.

class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'github', 'linkdin')
    list_display_links = ('id', 'github')
    
    
admin.site.register(Links, LinksAdmin)


# class YtAdmin(admin.ModelAdmin):
#     def myphoto(self, object):
#         return format_html('<img src="{}" width="40" />'.format(object.photo.url))

#     list_display = ('id', 'name', 'myphoto', 'subs_count', 'is_featured')
#     search_fields = ('name', 'camera_type')
#     list_filter = ('city', 'camera_type')
#     list_display_links = ('id', 'name')
#     list_editable = ('is_featured',)


# admin.site.register(Youtuber, YtAdmin)