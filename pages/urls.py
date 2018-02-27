from django.urls import path

from . import views


urlpatterns = [
	path('', views.home_view, name='home'),
	path('page/<int:page>', views.home_view, name='home'),
	path('about/', views.about_view, name='about'),
	path('post/<slug:slug>/', views.post_detail_view, name='post_detail'),
	path('post/<slug:slug>/edit', views.post_edit_view, name='post_edit'),
	path('post_create/', views.post_create_view, name='post_create'),
	path('post/<slug:slug>/delete', views.post_delete_view, name='post_delete'),
]