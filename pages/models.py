from django.db import models
from django.contrib.auth.models import User

import datetime


class PublicManager(models.Manager):
	"""Returns published posts that are not in the future."""

	def published(self):
		PUBLIC = 1
		return self.get_queryset().filter(status=PUBLIC, publish__lte=datetime.datetime.now())


class Category(models.Model):
	"""Category model."""
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'
		db_table = 'title'
		ordering = ('title',)

	def __str__(self):
		return self.title


class DifficultyLevel(models.Model):
	"""Difficulty option Foreign Key model."""
	BEGINNER = 0
	INTERMEDIATE = 1
	ADVANCED = 2

	DIFFICULTY_CHOICES = (
		(BEGINNER, 'Beginner'),
		(INTERMEDIATE, 'Intermediate'),
		(ADVANCED, 'Advanced'),
	)
	dificulty_level = models.IntegerField(choices=DIFFICULTY_CHOICES, default=BEGINNER)

	def __str__(self):
		return self.DIFFICULTY_CHOICES[self.dificulty_level][1]


class PostType(models.Model):
	"""Difficulty option Foreign Key model."""
	ARTICLE = 0
	TWITTER = 1
	VIDEO = 2

	TYPE_CHOICES = (
		(ARTICLE, 'Article'),
		(TWITTER, 'Twitter'),
		(VIDEO, 'Video'),
	)
	post_type = models.IntegerField(choices=TYPE_CHOICES, default=ARTICLE)

	def __str__(self):
		"""Returns human-readable option in admin."""
		return self.TYPE_CHOICES[self.post_type][1]


class Post(models.Model):
	"""Post model."""
	STATUS_CHOICES = (
		(0, 'Draft'),
		(1, 'Public'),
	)

	title = models.CharField(max_length=280)
	slug = models.SlugField(max_length=200, unique_for_date='publish')
	url = models.URLField(max_length=250)
	description = models.TextField(null=True, blank=True)
	set_number = models.CharField(max_length=2) # 14 means 1rst post out of 4 - max 9 posts per day
	status = models.IntegerField(choices=STATUS_CHOICES, default=0)
	publish = models.DateTimeField(default=datetime.datetime.now)
	categories = models.ManyToManyField(Category, blank=True)
	difficulty_level = models.ForeignKey(DifficultyLevel, on_delete='SET_DEFAULT')
	post_type = models.ForeignKey(PostType, on_delete='SET_DEFAULT')

	author = models.ForeignKey(User, blank=True, null=True, on_delete='SET_DEFAULT')
	tease = models.TextField(blank=True, help_text='Concise text suggested. Does not appear in RSS feed.')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	seo_text = models.TextField(null=True, blank=True)
	
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



	
