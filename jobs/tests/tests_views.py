from django.test import TestCase, Client
from django.urls import reverse
# from django.forms.models import model_to_dict
# from django.db.models import Q

# from core.models import (
# 	Post, PostType, DifficultyLevel, Category, Link,ReviewedLink)
from django.contrib.auth.models import User

# from datetime import datetime
# from datetime import timedelta
# from django.utils import timezone



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