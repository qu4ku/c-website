from django.contrib import admin
from django.urls import path, include
from django.conf import settings



urlpatterns = [
    path('my_admin/', admin.site.urls),
    path('', include('pages.urls')),
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns