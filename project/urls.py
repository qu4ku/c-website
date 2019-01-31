from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .sitemaps import (
	PostSitemap, StaticSitemap, HomeSitemap, CategorySitemap, PostTypeSitemap,
	DifficultyLevelSitemap,
)


sitemaps = {
	'posts': PostSitemap,
	'pages': StaticSitemap,
	'home': HomeSitemap,
	'tags': CategorySitemap,
	'levels': DifficultyLevelSitemap,
	'type': PostTypeSitemap
}


urlpatterns = [
	path('my_admin/', admin.site.urls),
	path('', include('core.urls')),
	path('newsletter/', include('newsletter.urls')),
	path('jobs/', include('jobs.urls')),
	path('account/', include('account.urls')),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    	name='django.contrib.sitemaps.views.sitemap')

]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	# Media files are not, by default, served during development.
	] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

