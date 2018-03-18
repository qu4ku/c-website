from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

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
		print(form)
		context = {'form': form}
		template = 'profile_edit.html'

		return render(request, template, context)


def change_password_view(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		print(form)
		if form.is_valid():
			print('valid')
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('profile')
		else:
			print('invalid')
			return redirect('password_change')

	form = PasswordChangeForm(user=request.user)
	context = {'form': form}
	template = 'change_password.html'

	return render(request, template, context)