from django.contrib.sitemaps import Sitemap
from core.models import Post
from django.urls import reverse

from datetime import datetime


class PostsSitemap(Sitemap):
	changefreq = "never"
	priority = 0.5

	def items(self):
		return Post.published.all()

	def lastmod(self, obj):
		return obj.modified


class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['about', 'add_link', 'add_feedback', 'jobs']

    def location(self, item):
        return reverse(item)


class HomeSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


