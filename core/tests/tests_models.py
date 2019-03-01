from django.test import TestCase
from core.models import (Post, PostType, Category, DifficultyLevel, 
	get_default_publish_date)
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import timedelta


class TestModels(TestCase):

	def setUp(self):
		self.user = User.objects.create_user('test', 'test', 'test')
		self.user.save()
		self.client.login(username='test', password='test')

		# Test Post
		self.post_type, is_created = PostType.objects \
			.get_or_create(post_type='twitter')
		self.post_type = PostType.objects.get(post_type='twitter')
		self.difficulty_level, is_created = DifficultyLevel.objects \
			.get_or_create(difficulty_level='beginner')
		self.category, is_created = Category.objects \
			.get_or_create(title='testcategory', slug='testcategory')

		self.post = Post.objects.create(
			title='test project',
			set_number='13',
			publish = timezone.now(),
			status='public',
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)

	def test_set_number(self):
		self.assertEquals(self.post.set_number, '13')
		self.assertEquals(self.post.first_set_number, '1')
		self.assertEquals(self.post.second_set_number, '3')

	def test_post_on_save_slug_created(self):
		self.post2 = Post.objects.create(
			title='test project',
			set_number='13',
			publish = timezone.now(),
			status='public',
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)

		self.assertEquals(self.post.slug, 'test-project')
		self.assertEquals(self.post2.slug, 'test-project-cp-1')

	def test_post_on_save_twitter(self):
		self.post.url = 'https://twitter.com/qu4ku/status/1098790901978226688'
		post_type_twitter, is_created = PostType.objects.get_or_create(post_type='twitter')
		self.post.save()

		self.assertEquals(self.post_type, post_type_twitter)
		self.assertEquals(self.post.original_author_handle, 'qu4ku')
		self.assertEquals(
			self.post.original_author_url, 'https://twitter.com/qu4ku/')

	def test_post_on_save_video(self):
		self.post.url = 'https://www.youtube.com/watch?v=uvy9Cr_wTPI'
		post_type_video, is_created = PostType.objects.get_or_create(
			post_type='video')
		self.post.save()

		self.assertEquals(self.post.post_type, post_type_video)

	def test_post_on_save_post(self):
		self.post.url = 'https://soundcloud.com/a16z/cryptonetworks-economies-governance-capital-access-risk'
		post_type_podcast, is_created = PostType.objects.get_or_create(
			post_type='podcast')
		self.post.save()

		self.assertEquals(self.post.post_type, post_type_podcast)

	def test_get_default_publish_date_no_posts(self):
		posts = Post.objects.all()
		for post in posts:
			post.delete()
		self.assertEquals(Post.objects.all().count(), 0)

		today = timezone.now().replace(
			hour=6, minute=0, second=0, microsecond=0)
		self.assertEquals(get_default_publish_date(), today)

	def test_get_default_publish_date_two_posts(self):
		posts = Post.objects.all()
		for post in posts:
			post.delete()
		self.post1 = Post.objects.create(
			title='test project',
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)
		self.post2 = Post.objects.create(
			title='test project',
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)
		posts = Post.objects.all()
		# print(posts.count())
		self.assertEquals(Post.objects.all().count(), 2)

		last_date = posts[0].publish
		self.assertEquals(get_default_publish_date(), last_date)

	def test_get_default_publish_date_three_posts_same_day(self):
		posts = Post.objects.all()
		for post in posts:
			post.delete()
		self.post1 = Post.objects.create(
			title='test project',
			status='public',
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)
		self.post2 = Post.objects.create(
			title='test project',
			status='public',
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)
		self.post2 = Post.objects.create(
			title='test project',
			status='public',
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)

		posts = Post.objects.all()
		self.assertEquals(Post.objects.all().count(), 3)

		last_date = posts[0].publish
		last_date = last_date.replace(hour=6, minute=0, second=0, microsecond=0)
		next_day = last_date + timedelta(days=1)
		self.assertEquals(get_default_publish_date(), next_day)


	def test_get_default_publish_date_three_posts_diff_day(self):
		posts = Post.objects.all()
		for post in posts:
			post.delete()
		now = timezone.now()
		yesterday = now - timedelta(days=1)
		self.post1 = Post.objects.create(
			title='test project',
			status='public',
			publish=yesterday,
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)
		self.post2 = Post.objects.create(
			title='test project',
			status='public',
			publish=now,
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)
		self.post2 = Post.objects.create(
			title='test project',
			status='public',
			publish=now,
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)

		posts = Post.objects.all()
		self.assertEquals(Post.objects.all().count(), 3)

		last_date = posts[0].publish
		last_date = last_date.replace(hour=6, minute=0, second=0, microsecond=0)
		self.assertEquals(get_default_publish_date(), last_date)


