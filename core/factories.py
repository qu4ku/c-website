import factory
from factory.django import DjangoModelFactory

from . import models


class PostFactory(DjangoModelFactory):
	class Meta:
		model = models.Post

		