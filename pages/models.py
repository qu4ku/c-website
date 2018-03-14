from django.contrib.auth.models import User
from django.db import models


import datetime
from django.utils import timezone


class PublicManager(models.Manager):
	"""Returns published posts that are not in the future."""

	def published(self):
		return self.get_queryset().filter(status='Public', publish__lte=timezone.now())


class Category(models.Model):
	"""Category model."""

	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	description = models.CharField(max_length=250, blank=True, null=True)
	seo_title = models.CharField(max_length=60, blank=True, null=True)
	seo_description = models.CharField(max_length=165, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'
		db_table = 'title'
		ordering = ('title',)

	def __str__(self):
		return self.title


class DifficultyLevel(models.Model):
	"""Difficulty option Foreign Key model."""

	DIFFICULTY_CHOICES = (
		('Beginner', 'Beginner'),
		('Intermediate', 'Intermediate'),
		('Advanced', 'Advanced'),
	)
	dificulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='Beginner')

	def __str__(self):
		return self.dificulty_level


class PostType(models.Model):
	"""Difficulty option Foreign Key model."""

	TYPE_CHOICES = (
		('Article', 'Article'),
		('Twitter', 'Twitter'),
		('Video', 'Video'),
		('Podcast', 'Podcast'),
	)
	post_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Article')

	def __str__(self):
		"""Returns human-readable option in admin."""
		return self.post_type


class Post(models.Model):
	"""Post model."""

	STATUS_CHOICES = (
		('Draft', 'Draft'),
		('Public', 'Public'),
	)

	ACTIVE_CHOICES = (
		('Dead', 'Dead'),
		('Active', 'Active'),
	)

	title = models.CharField(max_length=280)
	slug = models.SlugField(max_length=280, unique_for_date='publish')
	url = models.URLField(max_length=250)
	description = models.TextField(null=True, blank=True)
	set_number = models.CharField(max_length=2) # 14 means 1rst post out of 4 - max 9 posts per day
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
	publish = models.DateTimeField(default=timezone.now)
	categories = models.ManyToManyField(Category, blank=True)
	difficulty_level = models.ForeignKey(DifficultyLevel, on_delete='SET_DEFAULT')
	post_type = models.ForeignKey(PostType, on_delete='SET_DEFAULT')

	author = models.ForeignKey(User, blank=True, null=True, on_delete='SET_DEFAULT')
	tease = models.TextField(blank=True, help_text='Concise text suggested. Does not appear in RSS feed.')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	seo_title = models.CharField(max_length=60, blank=True, null=True)
	seo_description = models.CharField(max_length=165, blank=True, null=True)

	active = models.CharField(max_length=20, choices=ACTIVE_CHOICES, default='Active')
	
	# Twitter case
	original_author = models.CharField(max_length=250, blank=True)
	original_author_handle = models.CharField(max_length=250, blank=True)
	original_author_url = models.URLField(max_length=250, blank=True)

	thumb_image = models.ImageField(upload_to='thumbs/', blank=True)

	# tags = TagField()
	objects = PublicManager()

	@property
	def first_set_number(self):
		"""Gets post's number in a certain day."""
		return self.set_number[0]

	@property
	def second_set_number(self):
		"""Gets number of posts in a certain day."""
		return self.set_number[1]

	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'
		db_table = 'posts'
		ordering = ('-publish',)
		get_latest_by = 'publish'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/post/{}/'.format(self.slug)

	def get_url_for_social(self):
		return 'https://www.knowledgeprotocol.com/post/{}/'.format(self.slug)


# 2do: LinkModel
class Link(models.Model):
	"""Link model."""
	ip = models.CharField(max_length=50, null=True)
	url = models.URLField(max_length=250)

class NewsletterContact(models.Model):
	"""Newsletter client model."""

	ip = models.CharField(max_length=50, null=True)
	email = models.EmailField(max_length=70, null=True, unique=True)

