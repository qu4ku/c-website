from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.models import User


def register_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = RegistrationForm()
		context = {
			'form': form
		}
		template = 'register.html'
		return render(request, template, context)


def profile_view(request):
	template = 'profile.html'
	context = {'user': request.user}
	return render(request, template, context)

def profile_edit_view(request):
	pass