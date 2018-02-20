from django.shortcuts import render

from .models import Post


def home_view(request):
	posts = Post.objects.all().order_by('-publish')
	template = 'home.html'
	context = {'posts': posts}
	
	return render(request, template, context)

def about(request):
	return render(request, 'about.html')
