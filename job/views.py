from django.shortcuts import render
from .models import job
# Create your views here.
def all_jobs(request):
    all_jobs = job.objects.all()
    context = {'jobs':all_jobs}
    return render(request,'job/jobs.html',context)


def job_details(request,pk):
    one_job = job.objects.get(id=pk)
    context = {'job':one_job}
    return render(request,'job/job_details.html',context)