from django.contrib import admin
from . models import *
from django.utils.html import format_html

# Register your models here.

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score', 'is_key_skill')
    list_display_links = ('id', 'name')
    

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    list_display_links = ('id', 'user')
    

@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','timestamp')
    list_display_links = ('id', 'name')
    

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name')
    

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.image.url))
    
    list_display = ('id','name', 'myphoto')
    list_display_links = ('id', 'name')
    

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.image.url))
    
    list_display = ('id','name','myphoto','date','is_active',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    list_display_links = ('id', 'name')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','academy','title', 'issue_date')
    list_display_links = ('id', 'academy')
    