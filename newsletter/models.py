from django.db import models


class NewsletterContact(models.Model):
	"""
	Newsletter contact model.
	"""
	ip = models.CharField(max_length=50, blank=True, null=True)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField(max_length=70, unique=True)
	date_subscribed = models.DateTimeField(auto_now_add=True)
	date_unsubscribed = models.DateTimeField(null=True, blank=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = 'Newsletter Contact'
		verbose_name_plural = 'Newsletter Contacts'
		db_table = 'newsletter_contacts'
		ordering = ('-date_subscribed',)

