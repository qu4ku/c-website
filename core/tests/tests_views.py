from django.test import TestCase, Client
from django.urls import reverse


from ..models import Post, PostType, DifficultyLevel, Category, Link, ReviewedLink
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
		self.post_type, is_created = PostType.objects.get_or_create(post_type='twitter')
		self.difficulty_level, is_created = DifficultyLevel.objects.get_or_create(difficulty_level='beginner')
		self.category, is_created = Category.objects.get_or_create(title='testcategory', slug='testcategory')

		self.test_post = Post.objects.create(
			title='project',
			slug='subpage',
			publish = timezone.now(),
			status='public',
			url='http://some.pl',
			difficulty_level=self.difficulty_level,
			post_type=self.post_type,
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
		self.assertEquals(Post.objects.filter(slug=self.test_post).exists(), False)
	
	def test_category_view_GET(self):
		url = reverse('category', kwargs={'slug': self.category.slug})
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'search_results.html')

	def test_level_view_GET(self):
		url = reverse('level', kwargs={'slug': self.difficulty_level})
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'search_results.html')


	def test_type_view_GET(self):
		url = reverse('type', kwargs={'slug': self.post_type})
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'search_results.html')

	def test_search_GET(self):
		url = reverse('search')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'search_results.html')

	def test_add_link_GET(self):
		url = reverse('add_link')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'add_link.html')

	def test_add_link_thanks_GET(self):
		url = reverse('add_link_thanks')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'add_link_thanks.html')

	def test_add_feedback_GET(self):
		url = reverse('add_feedback')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'add_feedback.html')

	def test_feedback_thanks_GET(self):
		url = reverse('add_feedback_thanks')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'feedback_thanks.html')

	def test_feedbacks_GET(self):
		url = reverse('feedbacks')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'feedbacks.html')

	def test_tags_GET(self):
		url = reverse('tags')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'tags.html')

	def test_review_link_GET(self):
		url = reverse('review_link')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'link_review.html')

	def test_review_link_POST_post_new_url(self):
		url = reverse('review_link')
		url_to_review = 'https://twitter.com/muneeb/status/1082413835179474945'
		response = self.client.post(url, {
				'url': url_to_review, 
			})

		self.assertEquals(response.status_code, 200)
		self.assertEquals(ReviewedLink.objects.first().url, url_to_review)

	def test_review_link_POST_post_no_url(self):
		url = reverse('review_link')
		url_to_review = ''
		response = self.client.post(url, {
				'url': url_to_review, 
			})

		self.assertEquals(response.status_code, 302)

	def test_review_link_POST_post_url_in_posted(self):
		url = reverse('review_link')
		url_to_review = 'http://some.pl'
		response = self.client.post(url, {
				'url': url_to_review, 
			})

		self.assertEquals(response.status_code, 200)
		self.assertEquals(Post.objects.filter(url=url_to_review).first().url, url_to_review)
		self.assertContains(response, 'Link already in posted links.')

	def test_review_link_POST_post_url_in_listed(self):
		url = reverse('review_link')
		url_to_review = 'http://inlink.pl'

		Link.objects.create(url=url_to_review)

		response = self.client.post(url, {
				'url': url_to_review, 
			})

		self.assertEquals(response.status_code, 200)
		self.assertContains(response, 'Link already in submitted links.')

	def test_review_link_POST_post_url_in_reviewed(self):
		url = reverse('review_link')
		url_to_review = 'http://inreviewed.pl'

		ReviewedLink.objects.create(url=url_to_review)

		response = self.client.post(url, {
				'url': url_to_review, 
			})

		self.assertEquals(response.status_code, 200)
		self.assertContains(response, 'Link already in reviewed links.')

	# to be done
	def post_edit_view_POST_valid(self):
		url = reverse('edit_post', {'slug': self.test_post.slug})

		response = self.client.post(url, {

			})
		self.assertEquals(response.status_code, 200)

	# def post_edit_view_POST_invalid(self):



