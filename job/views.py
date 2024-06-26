from django.shortcuts import redirect, render
from django.urls import reverse
from .models import job
from accounts.models import profile
from django.core.paginator import Paginator
from .form import ApplyForm ,AddJob
from django.contrib.auth.decorators import login_required 
from .filters import JobFilter
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings




# Create your views here.
def all_jobs(request):
    all_jobs = job.objects.all().order_by('-puplished_at')
    filter = JobFilter(request.GET,queryset=all_jobs)
    all_jobs = filter.qs
    num = job.objects.all().order_by("-puplished_at")[:3]
    num1 = job.objects.all().count()
    data_per_page = Paginator(all_jobs,3)#this line will appear only on job in each page
    page_num = request.GET.get("page")
    page_obj = data_per_page.get_page(page_num)
    context = {'jobs':page_obj, 'num':num,'num1':num1,'filter':filter}
    return render(request,'job/jobs.html',context)

@login_required
def job_details(request,slug):
    one_job = job.objects.get(slug=slug)
    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_job = form.save(commit=False)
            my_job.apply_job = one_job
            my_job.save()
    else:
        form=ApplyForm()

    context = {'job':one_job,'form':form}
    return render(request,'job/job_details.html',context)


@login_required
def add_job(request):
    if request.method =="POST":
        form = AddJob(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.profile_name = profile.objects.get(user=request.user)
            myform.save()
            return redirect(reverse("job:all_jobs"))
    else:
        form=AddJob()
    
    return render(request,"job/add_job.html",{'form':form})



