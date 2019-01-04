# django 2.1 - new syntax
from django.urls import path
from django.contrib.auth.views import(
	PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
)
from django.contrib.auth import login, logout 

from . import views


urlpatterns = [
	path('login/', login, {'template_name': 'login.html'}, name='login'),
	path('logout/', logout, {'template_name': 'logout.html'}, name='logout'),
	path('register/', views.register_view, name='register'),
	path('profile/', views.profile_view, name='profile'),
	path('profile/edit/', views.profile_edit_view, name='profile_edit'),
	path('password-change/', views.change_password_view, name='password_change'),

	path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html')),
	path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done_form.html')),
	path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm_form.html')),
	path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete_form.html')),
]
