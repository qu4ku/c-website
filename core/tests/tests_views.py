from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post, PostType, DifficultyLevel
from datetime import datetime
from django.utils import timezone


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()

		# Test Post
		post_type, created = PostType.objects.get_or_create(post_type='twitter')
		difficulty_level, created = DifficultyLevel.objects.get_or_create(difficulty_level='beginner')
		try:
			self.test_post = Post.objects.create(
				title='project',
				slug='subpage',
				publish = timezone.now(),
				url='http://some.pl',
				difficulty_level=difficulty_level,
				post_type=post_type,
			)
		except:
			print('no')
		# print(self.test_post.get_absolute_url())
		# print(self.test_post.slug)

		# test = Post.objects.get(slug='some-slug')
		print(self.test_post)

	def test_home_view_GET(self):
		response = self.client.get(reverse('home'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')

	def test_about_view_GET(self):
		response = self.client.get(reverse('about'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'about.html')

	def test_post_detail_view_GET(self):
		post_type, created = PostType.objects.get_or_create(post_type='twitter')
		difficulty_level, created = DifficultyLevel.objects.get_or_create(difficulty_level='beginner')
		self.test_post = Post.objects.create(
			title='project',
			slug='subpage',
			publish = timezone.now(),
			url='http://some.pl',
			difficulty_level=difficulty_level,
			post_type=post_type,
		)

		print()
		# test = Post.objects.get(slug='some-slug')
		# print(test.slug)
		print(self.client.get('post/subpage'))
		url = reverse('post_detail', kwargs={'slug': 'subpage'})
		print(url)
		response = self.client.get(url)
		print(response)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'post_detail.html')

	# def test_post_detail_view_edit_GET(self):
	# 	response = self.client.get(reverse('post_edit', args=['some-slug']))

	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'post_edit.html', args=['some-slug'])

	# def test_post_delete_view_GET(self):
	# 	response = self.client.get(reverse('post_delete', args=['some-slug']))

	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'post_delete.html')