from django.contrib.sitemaps import Sitemap
from core.models import Post


class PostsSitemap(Sitemap):
	changefreq = "never"
	priority = 0.5

	def items(self):
		return Post.published.all()

	def lastmod(self, obj):
		return obj.modified

