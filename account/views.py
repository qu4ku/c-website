from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from .forms import RegistrationForm, EditProfileForm


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
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		
		if form.is_valid():
			form.save()

			return redirect('profile')
	else:
		form = EditProfileForm(instance=request.user)
		context = {'form': form}
		template = 'profile_edit.html'

		return render(request, template, context)
