from django.urls import path

from . import views
from .forms import PostForm


urlpatterns = [
	path('', views.home_view, name='home'),
	path('page/<int:page>', views.home_view, name='home'),
	path('about/', views.about, name='about'),
	path('article/<slug:slug>/', views.article_detail_view, name='article_detail'),
	path('twitter/<slug:slug>/', views.twitter_detail_view, name='twitter_detail'),
	path('video/<slug:slug>/', views.video_detail_view, name='video_detail'),
	path('create_post/', views.create_post_view, name='create_post'),
]