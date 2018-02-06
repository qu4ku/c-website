from django.shortcuts import render

from .models import Post


def home_view(request):
	posts = Post.objects.all().order_by('-post_date')
	context = {'posts': posts}
	
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html')
