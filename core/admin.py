from django.contrib import admin
from django import forms

from .models import Post, DifficultyLevel, PostType, Category, Link, Feedback, ReviewedLink


class PostAdminForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = '__all__'
		widgets = {
			'categories': forms.SelectMultiple(attrs={'size': 28}),
		}

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'set_number', 'publish', 'status', 'post_type']
	list_editable = ['status','set_number', 'publish']
	list_filter = ['status', 'publish', 'post_type', 'difficulty_level', 'categories']
	search_fields = ['title', 'description']
	list_per_page = 30

	form = PostAdminForm

	class Meta:
		model = Post


class LinkAdmin(admin.ModelAdmin):
	list_display = ['url', 'description']


class ReviewedLinkAdmin(admin.ModelAdmin):
	list_display = ['url']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(DifficultyLevel)
admin.site.register(PostType)
admin.site.register(Link, LinkAdmin)
admin.site.register(Feedback)
admin.site.register(ReviewedLink, ReviewedLinkAdmin)
