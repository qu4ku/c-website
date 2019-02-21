from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post, PostType, DifficultyLevel


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()

		# Test Post
		PostType.objects.create(post_type='twitter')
		DifficultyLevel.objects.create(difficulty_level='beginner')
		self.test_post = Post.objects.create(
			title='project',
			slug='some-slug',
			url='http://some.pl',
			difficulty_level=DifficultyLevel.objects.get(difficulty_level='beginner'),
			post_type=PostType.objects.get(post_type='twitter'),
		)
		print(self.test_post.get_absolute_url())

	def test_home_view_GET(self):
		response = self.client.get(reverse('home'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')

	def test_about_view_GET(self):
		response = self.client.get(reverse('about'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'about.html')

	def test_post_detail_view_GET(self):
		response = self.client.get(reverse('post_detail', args=['some-slug']))
		print(reverse('post_detail', args=['some-slug']))
		print(response)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'post_detail.html')

	def test_post_detail_view_edit_GET(self):
		response = self.client.get(reverse('post_edit', args=['some-slug']))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'post_edit.html', args=['some-slug'])

	# def test_post_delete_view_GET(self):
	# 	response = self.client.get(reverse('post_delete', args=['some-slug']))

	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'post_delete.html')