from django import forms


from .models import Post, NewsletterContact



class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'title',
			'slug',
			'url',
			'description',
			'set_number',
			'status',
			'publish',
			'categories',
			'difficulty_level',
			'post_type',
			# 'author',
			'tease',
			# 'created',
			# 'modified',
			
			'original_author',
			'original_author_handle',
			'original_author_url',
			'thumb_image',
		]

class NewsletterBoxForm(forms.ModelForm):
	class Meta:
		model = NewsletterContact
		fields = ['email', 'ip']