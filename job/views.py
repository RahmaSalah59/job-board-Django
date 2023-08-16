from django.shortcuts import render
from .models import job
from django.core.paginator import Paginator
from .form import ApplyForm

# Create your views here.
def all_jobs(request):
    all_jobs = job.objects.all()
    num = job.objects.all()
    data_per_page = Paginator(all_jobs,1)#this line will appear only on job in each page
    page_num = request.GET.get("page")
    page_obj = data_per_page.get_page(page_num)
    context = {'jobs':page_obj, 'num':num}
    return render(request,'job/jobs.html',context)


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