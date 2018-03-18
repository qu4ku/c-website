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
	path('password-change/', views.change_password_view, name='password_change'),

	path('password-reset/', password_reset, name='password_reset'),
	path('password-reset/done/', password_reset_done, name='password_reset_done'),
	path('password-reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
	path('password-reset/complete/', password_reset_complete, name='password_reset_complete'),
]
