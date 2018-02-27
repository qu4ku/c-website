from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

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


def about_view(request):
	return render(request, 'about.html')


def post_detail_view(request, slug):
	template = 'post_detail.html'
	post = Post.objects.published().get(slug=slug)

	context = {'post': post}

	return render(request, template, context)


def post_create_view(request):
	form = PostForm(request.POST or None)
	context = {'form': form}
	template = 'post_create.html'

	if form.is_valid():
		post = form.save(commit=False)
		post.save()
		messages.success(request, 'Successfully Created')
		return HttpResponseRedirect(post.get_absolute_url())
	else:
		messages.error(request, "Error")

	return render(request, template, context)


def post_edit_view(request, slug=None):
	post = get_object_or_404(Post, slug=slug)

	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)

		if form.is_valid():
			post.save()
			messages.success(request, 'Saved')
			return HttpResponseRedirect(post.get_absolute_url())
	else:
		form = PostForm(instance=post)

	context = {
		'post': post,
		'form': form,
	}
	template = 'post_edit.html'
	return render(request, template, context)


def post_delete_view(request, slug=None):
	post = get_object_or_404(Post, slug=slug)
	post.delete()
	messages.success(request, 'Deleted')
	return redirect('home')

