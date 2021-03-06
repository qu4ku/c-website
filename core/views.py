from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

from .models import (Post, Category, DifficultyLevel, Feedback, PostType,
	ReviewedLink, Link)
from .forms import PostForm, LinkForm, FeedbackForm, ReviewedLinkForm


def home_view(request):
	post_list = Post.published.all()
	query = request.GET.get('q')  # Search

	if query:
		# Check both title and description for the query word
		post_list = Post.published.filter(
			Q(title__icontains=query) |
			Q(description__icontains=query)
		).distinct()

	paginator = Paginator(post_list, 18)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	template = 'home.html'
	context = {
		'posts': posts,
	}

	return render(request, template, context)


def about_view(request):
	return render(request, 'about.html')


def post_detail_view(request, slug):
	template = 'post_detail.html'
	post = get_object_or_404(Post, slug=slug, status='public')
	categories = post.categories.all()  # Get categories objects

	categories_dict = {}
	post_cap = 3
	for category in categories:
		top_posts = Post.objects.all().filter(categories=category)[:post_cap]
		categories_dict[category] = top_posts

	context = {
		'post': post,
		'categories': categories_dict,
		}

	return render(request, template, context)


@login_required
def post_create_view(request):
	form = PostForm(request.POST or None, request.FILES or None)
	context = {'form': form}
	template = 'post_create.html'

	if form.is_valid():
		post = form.save(commit=False)
		post.save()
		# Messages are not used right now
		messages.success(request, 'Successfully Created')
		return redirect(reverse('post_create'))
	else:
		messages.error(request, "Error")

	return render(request, template, context)


@login_required
def post_edit_view(request, slug=None):
	post = get_object_or_404(Post, slug=slug)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)

		if form.is_valid():
			post.save()
			messages.success(request, 'Saved')
			return redirect(post.get_absolute_url())
	else:
		form = PostForm(instance=post)

	context = {
		'post': post,
		'form': form,
	}
	template = 'post_edit.html'
	return render(request, template, context)


@login_required
def post_delete_view(request, slug=None):
	post = get_object_or_404(Post, slug=slug)
	post.delete()
	messages.success(request, 'Deleted')
	return redirect('home')


def category_view(request, slug):
	category = get_object_or_404(Category, slug=slug)
	post_list = Post.published.filter(categories=category)

	paginator = Paginator(post_list, 18)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	template = 'search_results.html'
	context = {
		'posts': posts,
		'category': category,
		'category_description': category.description,
	}

	return render(request, template, context)


def level_view(request, slug):
	level = get_object_or_404(DifficultyLevel, difficulty_level=slug)
	post_list = Post.published.filter(difficulty_level=level)

	paginator = Paginator(post_list, 18)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	template = 'search_results.html'
	context = {
		'posts': posts,
		'level': level,
	}

	return render(request, template, context)


def type_view(request, slug):

	post_type = get_object_or_404(PostType, post_type=slug)
	post_list = Post.published.filter(post_type=post_type)

	paginator = Paginator(post_list, 18)  # Show 25 contacts per page
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	template = 'search_results.html'
	context = {
		'posts': posts,
		'type': post_type,
	}

	return render(request, template, context)


def search_view(request):
	post_list = Post.published.all()
	query = request.GET.get('q')  # Search

	if query:
		# Check both title and description for the query word
		post_list = Post.published.filter(
			Q(title__icontains=query) | 
			Q(description__icontains=query)
		).distinct()

	paginator = Paginator(post_list, 18)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	template = 'search_results.html'
	context = {
		'posts': posts,
		'query': query,
	}

	return render(request, template, context)


def add_link_view(request):
	form = LinkForm(request.POST or None)
	context = {'form': form}
	template = 'add_link.html'

	if form.is_valid():
		post = form.save(commit=False)
		ip = request.META.get('REMOTE_ADDR', None)
		post.ip = ip
		post.save()
		# Messages are not used right now
		messages.success(request, 'Link added.')
		return redirect(reverse('add_link_thanks'))
	else:
		messages.error(request, "Error")

	return render(request, template, context)


def add_link_thanks_view(request):
	context = {}
	template = 'add_link_thanks.html'

	return render(request, template, context)


def add_feedback_view(request):
	form = FeedbackForm(request.POST or None)
	context = {'form': form}
	template = 'add_feedback.html'

	if form.is_valid():
		post = form.save(commit=False)
		ip = request.META.get('REMOTE_ADDR', None)
		post.ip = ip
		post.save()
		# Messages are not used right now
		messages.success(request, 'Feedback added.')
		return redirect(reverse('add_feedback_thanks'))
	else:
		messages.error(request, "Error")

	return render(request, template, context)


@login_required
def feedbacks_view(request):
	feedbacks = Feedback.objects.all()[::-1]
	context = {'feedbacks': feedbacks}
	template = 'feedbacks.html'

	return render(request, template, context)


def add_feedback_thanks_view(request):
	template = 'feedback_thanks.html'

	return render(request, template)


def tags_view(request):
	tags = Category.objects.all()
	template = 'tags.html'
	context = {
		'tags': tags,
	}

	return render(request, template, context)


@login_required
def review_link_view(request):
	template = 'link_review.html'

	if request.method == 'GET':
		return render(request, template)
	elif request.method == 'POST':
		link_to_review = request.POST.get('url', None)
		if not link_to_review:
			return redirect(reverse('review_link'), template)
		is_posted = Post.objects.filter(url=link_to_review).exists()
		is_listed = Link.objects.filter(url=link_to_review).exists()
		is_reviewed = ReviewedLink.objects.filter(url=link_to_review).exists()

		if is_posted:
			msg = 'Link already in posted links.'
		elif is_listed:
			msg = 'Link already in submitted links.'
		elif is_reviewed:
			msg = 'Link already in reviewed links.'
		else:
			new_link = ReviewedLinkForm(request.POST)
			new_link.save()
			msg = 'New link. Added to the reviewed.'
		context = {
			'link_to_review': link_to_review,
			'msg': msg,
		}
		return render(request, template, context)

