from django.test import TestCase
from django.utils import timezone

from core.forms import PostForm
from core.models import Post, Category, DifficultyLevel, PostType
from django.contrib.auth.models import User

from django.forms.models import model_to_dict


class TestForms(TestCase):

	def setUp(self):
		self.user = User.objects.create_user('test', 'test', 'test')
		self.user.save()
		self.client.login(username='test', password='test')

		# Test Post
		self.post_type, is_created = PostType.objects \
			.get_or_create(post_type='twitter')
		print(self.post_type)
		self.post_type = PostType.objects.get(post_type='twitter')
		self.difficulty_level, is_created = DifficultyLevel.objects \
			.get_or_create(difficulty_level='beginner')
		self.category, is_created = Category.objects \
			.get_or_create(title='testcategory', slug='testcategory')

		self.post = Post.objects.create(
			title='project',
			slug='subpage',
			publish = timezone.now(),
			status='public',
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
		)
	# to be done: figure out how to send manytomany field as data
	"""
	def test_post_form_valid_data(self):

		form = PostForm(data={
			'title': self.post.title,
			'slug': 'new-slug',
			'url': self.post.url,
			'description': self.post.description,
			'set_number': self.post.set_number,
			'status': self.post.status,
			'publish': self.post.publish,
			'categories': self.post.categories,
			# 'difficulty_level': self.post.difficulty_level,
			'difficulty_level': DifficultyLevel.objects.all().first(),
			'post_type': self.post.post_type,
			# 'post_type': 'twitter',
			'seo_title': self.post.seo_title,
			})
		print(DifficultyLevel.objects.all().first())
		print(form.errors)

		self.assertTrue(form.is_valid())
	"""