from django import forms


from .models import NewsletterContact


class NewsletterBoxForm(forms.ModelForm):
	class Meta:
		model = NewsletterContact
		fields = ['email', 'ip']

		widgets = {
			'email': forms.TextInput(attrs={'class': 'form__text-input', 'autofocus': 'none'}),
			
		}