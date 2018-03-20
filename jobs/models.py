from django.db import models
from django.utils import timezone


# Create your models here.
def thirty_days_hence():
	return timezone.now() + timezone.timedelta(days=30)


class Company(models.Model):
	"""
	Company model.
	"""
	company_name = models.CharField(max_length=255)


class JobTag(models.Model):
	"""
	Category model.
	"""
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Job Tag'
		verbose_name_plural = 'Job Tags'
		db_table = 'job_tag'
		ordering = ('title',)

	def __str__(self):
		return self.title


class Job(models.Model):
	"""
	Job model.
	"""
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	start_date = models.DateTimeField(default=timezone.now)
	end_date = models.DateTimeField(default=thirty_days_hence)
	is_active = models.BooleanField(default=False)
	is_payed = models.BooleanField(default=False)
	is_highlighted = models.BooleanField(default=False)
	company = models.ForeignKey(Company, on_delete='CASCADE')
	tag = models.ManyToManyField(JobTag, blank=True)
