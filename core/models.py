from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import datetime
from datetime import timedelta
from django.utils.text import slugify
from unidecode import unidecode
import re


def default_start_time():
	now = timezone.now()
	start = now.replace(hour=6, minute=0, second=0, microsecond=0)
	return start

def get_default_day():
	"""
	Gets default day for a publish field. 
	Checks last updated day in the database and returns either the same date,
	or next day if there are 3 posts with such date.
	"""
	posts = Post.objects.all()
	if not posts:
		return timezone.now()

	last_date = posts[0].publish
	last_date = last_date.replace(hour=6, minute=0, second=0, microsecond=0)
	
	# If three last posts have the same publish days means current post is for
	# the next day
	if posts[0].publish.day == posts[1].publish.day == posts[2].publish.day:
		date = last_date + timedelta(days=1)
		date = date.replace(hour=6, minute=0, second=0, microsecond=0)
		return date
	else: 
		return last_date


def get_default_number():
	"""
	Gets default number for set_number field.
	"""
	posts = Post.objects.all()
	if not posts:
		return ''
	day0 = posts[0].publish.day
	day1 = posts[1].publish.day
	day2 = posts[2].publish.day

	
	# Last three days have the same day, mans current post if first one in the next day 
	if day0 == day1 == day2:
		return '13'
	elif day0 == day1 != day2:  #  Two the same days means current is third one
		return '33'
	elif day0 != day1 == day2:
		return '23'
	else:
		return ''


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

	def get_absolute_url(self):
		return '/category/{}/'.format(self.slug)



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

	def get_absolute_url(self):
		return '/level/{}/'.format(self.difficulty_level)


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

	def get_absolute_url(self):
		return '/type/{}/'.format(self.post_type)


class Post(models.Model):
	"""
	Post model.
	"""
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('public', 'Public'),
	)

	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
	# publish = models.DateTimeField(default=default_start_time)
	publish = models.DateTimeField(default=get_default_day)
	set_number = models.CharField(max_length=2, default=get_default_number) # 14 = 1 out of 4. max 9 posts per day.
	title = models.CharField(max_length=280)
	url = models.URLField(max_length=250)
	slug = models.SlugField(max_length=280, unique=True, blank=True, default='')
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

	def save(self, *args, **kwargs):
		# Slugify the title if slug not provided
		if not self.slug:
			base_slug = slugify(unidecode(self.title))
			new_slug = base_slug
			counter = 0
			while Post.objects.filter(slug=new_slug).exists():
				counter += 1
				new_slug = '{}-cp-{}'.format(base_slug, str(counter))
				print(new_slug)

			self.slug = new_slug

		# Get autor_url and autor_handle from url + set post_type  
		if 'twitter' in self.url:
			author_url_re = re.findall(r'https://twitter.com/.*?/', self.url)
			if author_url_re:
				self.original_author_url = author_url_re[0]
			author_handle_re = re.findall(r'(?<=https://twitter.com/).*?(?=/)', self.url)
			if author_handle_re:
				self.original_author_handle = author_handle_re[0]
			self.post_type = PostType.objects.get(post_type='twitter')

		# Set pos_type to video if youtube in an url
		if 'youtube' in self.url:
			self.post_type = PostType.objects.get(post_type='video')

		# Set publish date based on number
		if self.set_number == '13':
			self.publish += timedelta(seconds=3)
		elif self.set_number == '23':
			self.publish += timedelta(seconds=2)

		super(Post, self).save(*args, **kwargs)


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


class ReviewedLink(models.Model):
	"""
	Reviewed Link model.
	"""
	url = models.URLField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.url
