from django.test import TestCase, Client
from django.urls import reverse
from django.forms.models import model_to_dict
from django.db.models import Q
from core.forms import PostForm

from core.models import (
	Post, PostType, DifficultyLevel, Category, Link,ReviewedLink)
from django.contrib.auth.models import User

from datetime import datetime
from datetime import timedelta
from django.utils import timezone



# class TestForms(TestCase):

# 	def setUp(self):
# 		self.client = Client()

# 		# Log in a user
# 		self.user = User.objects.create_user('test', 'test', 'test')
# 		self.user.save()
# 		self.client.login(username='test', password='test')

# 		# Test Post
# 		self.post_type, is_created = PostType.objects.get_or_create(
# 			post_type='twitter')
# 		self.difficulty_level, is_created = DifficultyLevel \
# 			.objects.get_or_create(difficulty_level='beginner')
# 		self.category, is_created = Category.objects.get_or_create(
# 			title='testcategory', slug='testcategory')

# 		self.post = Post.objects.create(
# 			title='project',
# 			slug='subpage',
# 			publish = timezone.now() - timedelta(days=1),
# 			status='public',
# 			url='http://some.pl',
# 			difficulty_level=self.difficulty_level,
# 			post_type=self.post_type,
# 		)
# 		self.post.categories.add(self.category)


# 	def test_post_form_valid_data(self):
# 		print(DifficultyLevel.objects.all()[0])
# 		print(DifficultyLevel.objects.all()[0].difficulty_level)
# 		print(DifficultyLevel.objects.all()[0].difficulty_level[0])
# 		form = PostForm(data={
# 			'title': self.post.title,
# 			'slug': 'new-slug',
# 			'url': self.post.url,
# 			'description': self.post.description,
# 			'set_number': self.post.set_number,
# 			'status': self.post.status,
# 			'publish': self.post.publish,
# 			'categories': [1],
# 			# 'difficulty_level': 1,
# 			'difficulty_level': DifficultyLevel.objects.all()[0].difficulty_level,
# 			'post_type': 1,
# 			'seo_title': self.post.seo_title,
# 			})
# 		print(form.errors)
# 		print()
# 		for choice in form.fields['difficulty_level'].choices:
# 			print(choice)

# 		self.assertTrue(form.is_valid())
# 		form.fields['difficulty_level'].choices[0]
# 	def test_post_create_view_form(self):
# 		url = reverse('post_create')
# 		payload ={
# 			'title': self.post.title,
# 			'slug': 'new-slug',
# 			'url': self.post.url,
# 			'description': self.post.description,
# 			'set_number': self.post.set_number,
# 			'status': self.post.status,
# 			'publish': self.post.publish,
# 			'categories': [1],
# 			'difficulty_level': 1,
# 			'post_type': 1,
# 			'seo_title': self.post.seo_title,
# 			}
# 		form = PostForm(data=payload)
# 		self.assertTrue(form.is_valid())

# 		response = self.client.post(url, payload)

# 		[print(x) for x in dir(response)]

# 		print(response.status_code)


