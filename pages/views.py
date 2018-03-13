from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Post
from .forms import PostForm

import datetime


def home_view(request):
	post_list = Post.objects.published().order_by('-publish')
	query = request.GET.get('q')  # Search

	if query:
		# Check both title and description for the query word
		post_list = Post.objects.published().filter(
			Q(title__icontains=query) | 
			Q(description__icontains=query)
		).distinct()

	paginator = Paginator(post_list, 20)  # Show 25 contacts per page
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	template = 'home.html'
	context = {
		'posts': posts,
	}

	print(request.META.get('REMOTE_ADDR', None))

	return render(request, template, context)


def about_view(request):
	return render(request, 'about.html')


def post_detail_view(request, slug):
	template = 'post_detail.html'
	post = Post.objects.published().get(slug=slug)

	context = {'post': post}

	return render(request, template, context)


@login_required()
def post_create_view(request):
	form = PostForm(request.POST or None, request.FILES or None)
	context = {'form': form}
	template = 'post_create.html'

	if form.is_valid():
		post = form.save(commit=False)
		post.save()
		messages.success(request, 'Successfully Created')
		return HttpResponseRedirect(reverse('home'))
	else:
		messages.error(request, "Error")

	return render(request, template, context)


@login_required()
def post_edit_view(request, slug=None):
	post = get_object_or_404(Post, slug=slug)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)

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


@login_required()
def post_delete_view(request, slug=None):
	post = get_object_or_404(Post, slug=slug)
	post.delete()
	messages.success(request, 'Deleted')
	return redirect('home')

