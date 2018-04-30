from django.contrib import admin

from .models import Post, DifficultyLevel, PostType, Category, Link, Feedback


class PostAdmin(admin.ModelAdmin):

	list_display = ['title', 'set_number', 'publish', 'status', 'post_type']
	list_editable = ['status','set_number', 'publish']
	list_filter = ['status', 'publish', 'post_type', 'difficulty_level', 'categories']
	search_fields = ['title', 'description']

	class Meta:
		model = Post


class LinkAdmin(admin.ModelAdmin):

	list_display = ['url', 'description']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(DifficultyLevel)
admin.site.register(PostType)
admin.site.register(Link, LinkAdmin)
admin.site.register(Feedback)
