from django.shortcuts import render

from .models import Post
from .forms import PostForm

import datetime


def home_view(request, page=1):

	posts = Post.objects.published().order_by('-publish')
	template = 'home.html'

	next_page = page + 1
	previous_page = 1 if page == 1 else page + 1

	context = {
		'posts': posts,
		'page': page,
		'next_page': next_page,
		'previous_page': previous_page,
	}

	return render(request, template, context)


def about(request):
	return render(request, 'about.html')


def article_detail_view(request, slug):
	template = 'article_detail.html'

	post = Post.objects.published().get(slug=slug)

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


def create_post_view(request):
	form = PostForm(request.POST or None)
	context = {'form': form}
	template = 'create_form.html'

	if form.is_valid():
		form.save()



	return render(request, template, context)


