from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete='CASCADE')
	description = models.CharField(max_length=200, default='')
	city = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	image = models.ImageField(upload_to='profile_images', blank=True)

	class Meta:
		verbose_name = 'User Profile'
		verbose_name_plural = 'User Profiles'
		db_table = 'user_profiles'

	def __str__(self):
		return self.user.username


def create_profile(sender, **kwargs):
	if kwargs['created']:
		UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
