from django.test import TestCase
from django.test import SimpleTestCase


class SimpleTest(SimpleTestCase):
	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)

	def test_about_page_status_code(self):
		response = self.client.get('/about/')
		self.assertEquals(response.status_code, 200)
