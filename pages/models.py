from django.db import models
from django.contrib.auth.models import User


# Simple model for a test 
class Post(models.Model):

	title = models.CharField(max_length=200)
	slug = models.SlugField()
	original_url = models.CharField(max_length=500)
	description = models.TextField(null=True, blank=True)
	post_date = models.DateTimeField()

	# Later we may need: author, original_date, original_author, post_type

	def __str__(self):
		return self.title
