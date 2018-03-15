from django.contrib.auth.models import User
from django.db import models


from django.utils import timezone


class PublicManager(models.Manager):
	"""
	Returns published posts that are not in the future.
	"""
	def published(self):
		return self.get_queryset().filter(status='public', publish__lte=timezone.now())


class Category(models.Model):
	"""
	Category model.
	"""
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	description = models.CharField(max_length=250, blank=True, null=True)
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

	ACTIVE_CHOICES = (
		('dead', 'Dead'),
		('active', 'Active'),
	)

	title = models.CharField(max_length=280)
	slug = models.SlugField(max_length=280, unique_for_date='publish')
	url = models.URLField(max_length=250)
	description = models.TextField(null=True, blank=True)
	set_number = models.CharField(max_length=2) # 14 = 1 out of 4. max 9 posts per day.
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
	publish = models.DateTimeField(default=timezone.now)
	categories = models.ManyToManyField(Category, blank=True)
	difficulty_level = models.ForeignKey(DifficultyLevel, on_delete='SET_DEFAULT')
	post_type = models.ForeignKey(PostType, on_delete='SET_DEFAULT')

	author = models.ForeignKey(User, blank=True, null=True, on_delete='SET_DEFAULT')
	tease = models.CharField(max_length=280, blank=True, help_text='Concise text suggested. Does not appear in RSS feed.')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	seo_title = models.CharField(max_length=60, blank=True, null=True)
	seo_description = models.CharField(max_length=165, blank=True, null=True)

	active = models.CharField(max_length=20, choices=ACTIVE_CHOICES, default='active')
	is_active = models.BooleanField(default=True)

	# Twitter case
	original_author = models.CharField(max_length=250, blank=True)
	original_author_handle = models.CharField(max_length=250, blank=True)
	original_author_url = models.URLField(max_length=250, blank=True)

	thumb_image = models.ImageField(upload_to='thumbs/', blank=True)

	# tags = TagField()
	objects = PublicManager()

	@property
	def first_set_number(self):
		"""
		Gets post's number in a certain day.
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


# 2do: LinkModel
class Link(models.Model):
	"""
	Link model.
	"""
	ip = models.CharField(max_length=50, null=True)
	url = models.URLField(max_length=250)


