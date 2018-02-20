from django.db import models
from django.contrib.auth.models import User

import datetime


class PublicManager(models.Manager):
	"""Returns published posts that are not in the future."""

	def published(self):
		return self.get_query_set().filter(status__gte=1, publish__lte=datetime.datetime.now())


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
		return self.TYPE_CHOICES[self.post_type][1]


class Post(models.Model):
	"""Post model."""
	STATUS_CHOICES = (
		(0, 'Draft'),
		(1, 'Public'),
	)

	title = models.CharField(max_length=250)
	slug = models.SlugField(unique_for_date='publish')
	author = models.ForeignKey(User, blank=True, null=True, on_delete='SET_DEFAULT')
	url = models.CharField(max_length=250)
	description = models.TextField(null=True, blank=True)
	tease = models.TextField(blank=True, help_text='Concise text suggested. Does not appear in RSS feed.')
	status = models.IntegerField(choices=STATUS_CHOICES, default=0)
	publish = models.DateTimeField(default=datetime.datetime.now)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField(Category, blank=True)
	difficulty_level = models.ForeignKey(DifficultyLevel, on_delete='SET_DEFAULT')
	post_type = models.ForeignKey(PostType, on_delete='SET_DEFAULT')

	# tags = TagField()
	objects = PublicManager()

	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'
		db_table = 'posts'
		ordering = ('-publish',)
		get_latest_by = 'publish'

	def __str__(self):
		return self.title

	





