from django.contrib.auth.models import User
from links.models import Links, Videos

def project_context(request):

	context = {
		'me': User.objects.first(),
		'you': Links.objects.all(),
		'all': Videos.objects.all(),
  
  
	}

	return context
