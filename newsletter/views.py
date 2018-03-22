from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import NewsletterBoxForm


def newsletter_signup_view(request):

	template = 'newsletter_thanks.html'
	context = {}

	if request.method == 'POST':
		form = NewsletterBoxForm(request.POST)

		if form.is_valid():
			contact = form.save(commit=False)
			ip = request.META.get('REMOTE_ADDR', None)
			contact.ip = ip
			contact.save()
			# messages.success(request, 'Successfully Created')
			# return HttpResponseRedirect(reverse('home'))
			return render(request, template, context)
		else:
			messages.error(request, "Error")

	return render(request, template, context)
