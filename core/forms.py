from django import forms


from .models import Post



class PostForm(forms.ModelForm):
	class Meta:
		model = Post

		# 2do: Use exclude = () instead.
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
			'author',
			# 'tease',
			# 'created',
			# 'modified',
			'seo_title',
			'seo_description',
			# 'is_active',
			# 'original_author',
			'original_author_handle',
			'original_author_url',
			'thumb_image',
		]
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form__text-input'}),
			'slug': forms.TextInput(attrs={'class': 'form__text-input'}),
			'url': forms.TextInput(attrs={'class': 'form__text-input'}),
			'description': forms.Textarea(attrs={'class': 'form__text-area'}),
			'set_number': forms.TextInput(attrs={'class': 'form__text-input'}),
			'status': forms.Select(attrs={'class': 'form__text-input'}),
			# 'publish': forms.SelectDateWidget(attrs={'class': 'form__text-input'}),
			'categories': forms.SelectMultiple(attrs={'class': 'form__text-input--multichoice'}),
			'difficulty_level': forms.Select(attrs={'class': 'form__text-input'}),
			'post_type': forms.Select(attrs={'class': 'form__text-input'}),
			'author': forms.Select(attrs={'class': 'form__text-input'}),
			'seo_title': forms.TextInput(attrs={'class': 'form__text-input'}),
			'seo_description': forms.TextInput(attrs={'class': 'form__text-input'}),
			'original_author_handle': forms.TextInput(attrs={'class': 'form__text-input'}),
			'original_author_url': forms.TextInput(attrs={'class': 'form__text-input'}),
		}






