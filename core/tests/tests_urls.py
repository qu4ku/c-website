from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import (home_view, about_view, post_detail_view, post_edit_view, 
		post_create_view, post_delete_view, category_view, level_view, type_view,
		search_view, add_link_view, add_link_thanks_view, add_feedback_view, add_feedback_thanks_view,
		feedbacks_view, tags_view, review_link_view,
)


class TestConnections(TestCase):

	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)

	def test_about_page_status_code(self):
		response = self.client.get('/about/')
		self.assertEquals(response.status_code, 200)


class TestUrlsResolves(SimpleTestCase):
	
	def test_home_url_resolves(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home_view)

	def test_about_page_resolves(self):
		url = reverse('about')
		self.assertEquals(resolve(url).func, about_view)

	def test_post_detail_resolves(self):
		url = reverse('post_detail', args=['some-slug'])
		self.assertEquals(resolve(url).func, post_detail_view)

	def test_post_edit_resolves(self):
		url = reverse('post_edit', args=['some-slug'])
		self.assertEquals(resolve(url).func, post_edit_view)

	def test_post_create_resolves(self):
		url = reverse('post_create')
		self.assertEquals(resolve(url).func, post_create_view)

	def test_post_delete_resolves(self):
		url = reverse('post_delete', args=['some-slug'])
		self.assertEquals(resolve(url).func, post_delete_view)

	def test_category_resolves(self):
		url = reverse('category', args=['some-slug'])
		self.assertEquals(resolve(url).func, category_view)

	def test_level_resolves(self):
		url = reverse('level', args=['some-slug'])
		self.assertEquals(resolve(url).func, level_view)

	def test_type_resolves(self):
		url = reverse('type', args=['some-slug'])
		self.assertEquals(resolve(url).func, type_view)

	def test_search_resolves(self):
		url = reverse('search')
		self.assertEquals(resolve(url).func, search_view)

	def test_add_link_resolves(self):
		url = reverse('add_link')
		self.assertEquals(resolve(url).func, add_link_view)

	def test_add_link_thanks_resolves(self):
		url = reverse('add_link_thanks')
		self.assertEquals(resolve(url).func, add_link_thanks_view)

	def test_add_feedback_resolves(self):
		url = reverse('add_feedback')
		self.assertEquals(resolve(url).func, add_feedback_view)

	def test_add_feedback_thanks_resolves(self):
		url = reverse('add_feedback_thanks')
		self.assertEquals(resolve(url).func, add_feedback_thanks_view)

	def test_feedbacks_resolves(self):
		url = reverse('feedbacks')
		self.assertEquals(resolve(url).func, feedbacks_view)
		
	def test_tags_resolves(self):
		url = reverse('tags')
		self.assertEquals(resolve(url).func, tags_view)

	def test_reveiew_link_resolves(self):
		url = reverse('review_link')
		self.assertEquals(resolve(url).func, review_link_view)