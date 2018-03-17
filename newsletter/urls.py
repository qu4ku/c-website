from django.urls import path

from . import views


urlpatterns = [
	path('signup/', views.newsletter_signup_view, name='newsletter_signup'),
]