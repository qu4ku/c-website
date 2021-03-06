from django.urls import path

from . import views


urlpatterns = [
	path('', views.home_view, name='home'),
	path('about/', views.about_view, name='about'),
	path('post/<slug:slug>/', views.post_detail_view, name='post_detail'),
	path('post/<slug:slug>/edit/', views.post_edit_view, name='post_edit'),
	path('create/',
		views.post_create_view, name='post_create'),
	path('post/<slug:slug>/delete/', 
		views.post_delete_view, name='post_delete'),
	path('category/<slug:slug>/', views.category_view, name='category'),
	path('level/<slug:slug>/', views.level_view, name='level'),
	path('type/<slug:slug>/', views.type_view, name='type'),
	path('results/', views.search_view, name='search'),
	path('add-link/', views.add_link_view, name='add_link'),
	path('add-link/thanks',
		views.add_link_thanks_view, name='add_link_thanks'),
	path('add-feedback/', views.add_feedback_view, name='add_feedback'),
	path('feedback/thanks', 
		views.add_feedback_thanks_view, name='add_feedback_thanks'),
	path('feedbacks/', views.feedbacks_view, name='feedbacks'),
	path('tags/', views.tags_view, name='tags'),
	path('review-link/', views.review_link_view, name='review_link'),
]