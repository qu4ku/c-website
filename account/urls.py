from django.urls import path
from django.contrib.auth.views import login, logout

from . import views


urlpatterns = [
	path('login/', login, {'template_name': 'login.html'}, name='login'),
	path('logout/', logout, {'template_name': 'logout.html'}, name='logout'),
	path('register/', views.register_view, name='register'),
	path('profile/', views.profile_view, name='profile'),
	path('profile/edit/', views.profile_edit_view, name='profile_edit'),
]
