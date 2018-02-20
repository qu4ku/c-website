from django.db import models
import datetime



class PublicManager(models.Manager):
	"""Returns published posts that are not in the future."""

	def published(self):
		return self.get_query_set().filter(status__gte=1, publish__lte=datetime.datetime.now())
