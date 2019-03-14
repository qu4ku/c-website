from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User


class TestViews(TestCase):
	def setUp(self):
		self.client = Client()

		# Log in a user
		self.user = User.objects.create_user('test', 'test', 'test')
		self.user.save()
		self.client.login(username='test', password='test')

	def test_jobs_view_GET(self):

		url = reverse('jobs')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'jobs.html')

	def test_add_job_view_GET(self):

		url = reverse('add_job')
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'add_job.html')