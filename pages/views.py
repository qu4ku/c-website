from django.shortcuts import render

from .models import Post


def home_view(request):
	posts = Post.objects.all().order_by('-publish')
	template = 'home.html'
	context = {'posts': posts}
	
	return render(request, template, context)

def about(request):
	return render(request, 'about.html')

def article_detail_view(request, slug):
	template = 'article_detail.html'

	# 2do: Change to published
	post = Post.objects.get(slug=slug)
	print(post)

	context = {'post': post}

	return render(request, template, context)

def video_detail_view(request, slug):
	template = 'video_detail.html'

	# 2do: Change to published
	post = Post.objects.get(slug=slug)
	print(post)

	context = {'post': post}

	return render(request, template, context)

def twitter_detail_view(request, slug):
	template = 'twitter_detail.html'

	# 2do: Change to published
	post = Post.objects.get(slug=slug)
	print(post)

	context = {'post': post}

	return render(request, template, context)

