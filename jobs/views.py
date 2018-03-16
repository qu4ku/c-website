from django.shortcuts import render


def jobs_view(request):
	return render(request, 'jobs.html')


def add_job_view(request):
	return render(request, 'add_job.html')