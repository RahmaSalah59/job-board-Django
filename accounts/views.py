from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import signupfrom ,profileform ,userform
from .models import profile
from django.contrib.auth import authenticate,login
from job.models import job

# Create your views here.



def signup(request):
    if request.method=='POST':
        form = signupfrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = signupfrom()
    return render (request,'registration/signup.html',{'form':form})
                


def user_profile(request):
    Profile= profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':Profile})



def job_posted_profile(request,pk):
    selected_job= job.objects.get(pk = pk)
    profile_1 = selected_job.profile_name
    Profile= profile.objects.get(user=request.user)
    if(Profile == profile_1):
            return render(request,'accounts/profile.html',{'profile':Profile})    
    return render(request,'accounts/profile_custom_view.html',{'profile':selected_job.profile_name})


def job_applicants(request,pk):
    selected_job= job.objects.get(pk = pk)
    applicants = selected_job.apply.all()
    return render(request,'accounts/job_applicants.html',{'applicants':applicants})



def user_posted_jobs(request):
    Profile= profile.objects.get(user=request.user)
    posted_jobs = Profile.job.all()
    return render(request,'accounts/pofile_posted_jobs.html',{'profile':Profile, 'posted':posted_jobs})


def profile_edit(request):
    Profile= profile.objects.get(user=request.user)
    if request.method=='POST':
       profile_form=profileform(request.POST,request.FILES,instance=Profile)
       user_form=userform(request.POST,instance=request.user) 
       if  profile_form.is_valid() and user_form.is_valid():
           user_form.save()
           profile_form.save(commit=False)
           profile_form.user=request.user
           profile_form.save() 
           return redirect(reverse('accounts:profile'))

    else:
        profile_form=profileform(instance=Profile)
        user_form=userform(instance=request.user)

    return render(request,'accounts/profile_edit.html',{"profileform":profile_form,'userform':user_form})
