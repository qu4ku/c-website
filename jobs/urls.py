from django.urls import path

from . import views


urlpatterns = [
	path('', views.jobs_view, name='jobs'),
	path('add_job/', views.add_job_view, name='add_job'),

]