from django.contrib.sitemaps import Sitemap
from core.models import Post, Category, PostType, DifficultyLevel
from django.urls import reverse


class PostSitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.5
	protocol = 'https'

	def items(self):
		return Post.published.all()

	def lastmod(self, obj):
		return obj.modified


class CategorySitemap(Sitemap):
	changefreq = 'monthly'
	priority = 0.5
	protocol = 'https'

	def items(self):
		return Category.objects.all()

	def lastmod(self, obj):
		return obj.updated


class PostTypeSitemap(Sitemap):
	changefreq = 'monthly'
	priority = 0.5
	protocol = 'https'

	def items(self):
		return PostType.objects.all()


class DifficultyLevelSitemap(Sitemap):
	changefreq = 'never'
	priority = 0.5
	protocol = 'https'

	def items(self):
		return DifficultyLevel.objects.all()


class StaticSitemap(Sitemap):
	priority = 0.5
	changefreq = 'weekly'
	protocol = 'https'

	def items(self):
		return ['about', 'add_link', 'add_feedback', 'jobs', 'tags']

	def location(self, item):
		return reverse(item)


class HomeSitemap(Sitemap):
	priority = 0.8
	changefreq = 'daily'
	protocol = 'https'

	def items(self):
		return ['home']

	def location(self, item):
		return reverse(item)


