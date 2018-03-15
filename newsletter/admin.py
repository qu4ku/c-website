from django.contrib import admin

from .models import NewsletterContact


class NewsletterContactAdmin(admin.ModelAdmin):
	list_display = ['email', 'date_subscribed', 'is_active', 'ip']


admin.site.register(NewsletterContact, NewsletterContactAdmin)
