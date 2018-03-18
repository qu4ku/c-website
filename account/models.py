from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete='CASCADE')
	description = models.CharField(max_length=200, default='')
	city = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	phoone = models.IntegerField(default=0)

	class Meta:
		verbose_name = 'User Profile'
		verbose_name_plural = 'User Profiles'
		db_table = 'user_profiles'
	# 2do: __str__ returns username 
	# def __str__(self):
	# 	return self.user

def create_profile(sender, **kwargs):
	if kwargs['created']:
		UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
