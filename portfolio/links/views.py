from django.shortcuts import render
from .models import Links, Videos
# Create your views here.

def links(request):
    links = Links.objects.all()
    data = {
        'links' : links, 
    }
    return render(request, 'main/footer.html', data)

def videos(request):
    videos = Videos.objects.all()
    data = {
        'videos' : videos, 
    }
    return render(request, 'main/portfolio-detail.html', data)