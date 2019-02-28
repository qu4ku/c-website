from django import forms


from .models import Post, Link, Feedback, ReviewedLink


class PostForm(forms.ModelForm):
	class Meta:
		model = Post

		exclude = [
			'tease',
			'created',
			'modified',
			'is_active',
			'original_author',
			'thumb_image',
			'seo_title',
			'seo_description',
			'author',
			'source_url',
		]

		widgets = {
			'title': forms.TextInput(
				attrs={'class': 'form__text-input'}),
			'slug': forms.TextInput(
				attrs={'class': 'form__text-input'}),
			'url': forms.TextInput(
				attrs={'class': 'form__text-input'}),
			'description': forms.Textarea(
				attrs={'class': 'form__text-area'}),
			'set_number': forms.TextInput(
				attrs={'class': 'form__text-input', 'cols': 1}),
			'status': forms.Select(
				attrs={'class': 'form__text-input'}),
			'publish': forms.DateTimeInput(
				attrs={'class': 'form__text-input'}),
			'categories': forms.SelectMultiple(
				attrs={'class': 'form__text-input--multichoice'}),
			'difficulty_level': forms.Select(
				attrs={'class': 'form__text-input'}),
			'post_type': forms.Select(
				attrs={'class': 'form__text-input'}),
			'author': forms.Select(
				attrs={'class': 'form__text-input'}),
			'seo_title': forms.TextInput(
				attrs={'class': 'form__text-input'}),
			'seo_description': forms.TextInput(
				attrs={'class': 'form__text-input'}),
			'original_author_handle': forms.TextInput(
				attrs={'class': 'form__text-input'}),
			'original_author_url': forms.TextInput(
				attrs={'class': 'form__text-input'}),
		}


class LinkForm(forms.ModelForm):
	class Meta:
		model = Link

		fields = ('url', 'description')

		widgets = {
			'url': forms.TextInput(attrs={'class': 'form__text-input'}),
			'description': forms.Textarea(attrs={'class': 'form__text-area'}),
		}


class ReviewedLinkForm(forms.ModelForm):
	class Meta:
		model = ReviewedLink

		fields = ('url',)

		widgets = {
			'url': forms.TextInput(attrs={'class': 'form__text-input'}),
		}


class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback

		fields = ('body',)

		widgets = {
			'body': forms.Textarea(attrs={'class': 'form__text-area'}),
		}
