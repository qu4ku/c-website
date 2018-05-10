from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import datetime


def default_start_time():
    now = datetime.now()
    start = now.replace(hour=6, minute=0, second=0, microsecond=0)
    return start


class PublicManager(models.Manager):
	"""
	Returns published posts that are not in the future.
	"""
	def get_queryset(self):
		return super(PublicManager, self).get_queryset().filter(status='public', publish__lte=timezone.now())


class Category(models.Model):
	"""
	Category model.
	"""
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	seo_title = models.CharField(max_length=60, blank=True, null=True)
	seo_description = models.CharField(max_length=165, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		db_table = 'title'
		ordering = ('title',)

	def __str__(self):
		return self.title


class DifficultyLevel(models.Model):
	"""
	Difficulty option Foreign Key model.
	"""
	DIFFICULTY_CHOICES = (
		('beginner', 'Beginner'),
		('intermediate', 'Intermediate'),
		('advanced', 'Advanced'),
	)
	difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')

	def __str__(self):
		return self.difficulty_level


class PostType(models.Model):
	"""
	Difficulty option Foreign Key model.
	"""
	TYPE_CHOICES = (
		('article', 'Article'),
		('twitter', 'Twitter'),
		('video', 'Video'),
		('podcast', 'Podcast'),
	)
	post_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='article')

	def __str__(self):
		"""Returns human-readable option in admin."""
		return self.post_type


class Post(models.Model):
	"""
	Post model.
	"""
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('public', 'Public'),
	)

	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
	publish = models.DateTimeField(default=default_start_time)
	set_number = models.CharField(max_length=2) # 14 = 1 out of 4. max 9 posts per day.
	title = models.CharField(max_length=280)
	url = models.URLField(max_length=250)
	slug = models.SlugField(max_length=280, unique=True)
	post_type = models.ForeignKey(PostType, on_delete='SET_DEFAULT', default=0)
	difficulty_level = models.ForeignKey(DifficultyLevel, on_delete='SET_DEFAULT', default=2)
	categories = models.ManyToManyField(Category, blank=True)
	description = models.TextField(null=True, blank=True)

	original_author_url = models.URLField(max_length=250, blank=True)
	original_author_handle = models.CharField(max_length=250, blank=True)

	seo_title = models.CharField(max_length=60, blank=True, null=True)
	seo_description = models.CharField(max_length=165, blank=True, null=True)
	is_active = models.BooleanField(default=True)

	# Additional 
	original_author = models.CharField(max_length=250, blank=True)
	thumb_image = models.ImageField(upload_to='thumbs/', blank=True, null=True)
	source_url = models.URLField(max_length=250, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	tease = models.CharField(max_length=280, blank=True, help_text='Concise text suggested. Does not appear in RSS feed.')
	author = models.ForeignKey(User, blank=True, null=True, on_delete='SET_DEFAULT')

	objects = models.Manager()
	published = PublicManager()

	@property
	def first_set_number(self):
		"""
		Gets post number in a certain day.
		"""
		return self.set_number[0]

	@property
	def second_set_number(self):
		"""
		Gets number of posts in a certain day.
		"""
		return self.set_number[1]

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		db_table = 'posts'
		ordering = ('-publish',)
		get_latest_by = 'publish'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/post/{}/'.format(self.slug)

	def get_url_for_social(self):
		return 'https://www.knowledgeprotocol.com/post/{}/'.format(self.slug)


class Feedback(models.Model):
	"""
	Feedback model.
	"""
	ip = models.GenericIPAddressField(blank=True, null=True)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}: {}'.format(self.ip, self.body[:20])


class Link(models.Model):
	"""
	Link model.
	"""
	ip = models.GenericIPAddressField(blank=True, null=True)
	url = models.URLField(max_length=250)
	description = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		 return self.url
