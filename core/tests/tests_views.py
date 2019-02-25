from django.test import TestCase, Client
from django.urls import reverse


from ..models import Post, PostType, DifficultyLevel
from django.contrib.auth.models import User

from datetime import datetime
from django.utils import timezone


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()

		# Log in a user
		self.user = User.objects.create_user('test', 'test', 'test')
		self.user.save()
		self.client.login(username='test', password='test')

		# Test Post
		post_type, is_created = PostType.objects.get_or_create(post_type='twitter')
		difficulty_level, is_created = DifficultyLevel.objects.get_or_create(difficulty_level='beginner')

		self.test_post = Post.objects.create(
			title='project',
			slug='subpage',
			publish = timezone.now(),
			status='public',
			url='http://some.pl',
			difficulty_level=difficulty_level,
			post_type=post_type,
		)

	def test_home_view_GET(self):
		response = self.client.get(reverse('home'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')

	def test_about_view_GET(self):
		response = self.client.get(reverse('about'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'about.html')

	def test_post_detail_view_GET(self):

		url = reverse('post_detail', kwargs={'slug': self.test_post.slug})
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'post_detail.html')

	def test_post_detail_view_edit_GET(self):
		response = self.client.get(reverse('post_edit', kwargs={'slug': self.test_post.slug}))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'post_edit.html')

	def test_post_delete_view_GET(self):
		response = self.client.get(reverse('post_delete', kwargs={'slug': self.test_post.slug}), follow=True)

		self.assertEquals(response.status_code, 200)
