from django.urls import path
from django.contrib.auth.views import (
	login, logout, password_reset, password_reset_done, password_reset_confirm, 
	password_reset_complete
)

from . import views


urlpatterns = [
	path('login/', login, {'template_name': 'login.html'}, name='login'),
	path('logout/', logout, {'template_name': 'logout.html'}, name='logout'),
	path('register/', views.register_view, name='register'),
	path('profile/', views.profile_view, name='profile'),
	path('profile/edit/', views.profile_edit_view, name='profile_edit'),
	path('change-password/', views.change_password_view, name='password_change'),
	path('reset-password/', password_reset, name='password_reset'),
	# Need to use standard django name here
	path('reset-password/done/', password_reset_done, name='password_reset_done'),
	path('reset-password/confirm/', password_reset_confirm, name='password_reset_confirm'),
	path('reset-password/complete/', password_reset_complete, name='password_reset_complete'),
]
