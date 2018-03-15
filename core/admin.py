from django.contrib import admin

from .models import Post, DifficultyLevel, PostType, Category


class PostAdmin(admin.ModelAdmin):

	list_display = ['title', 'status', 'publish', 'set_number', 'post_type']
	list_editable = ['set_number', 'publish']
	list_filter = ['status', 'publish', 'post_type', 'difficulty_level', 'categories']
	search_fields = ['title', 'description']

	class Meta:
		model = Post


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(DifficultyLevel)
admin.site.register(PostType)