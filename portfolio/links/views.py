from django.shortcuts import render
from .models import Links
# Create your views here.

def links(request):
    links = Links.objects.all()
    data = {
        'links' : links, 
    }
    return render(request, 'main/footer.html', data)
