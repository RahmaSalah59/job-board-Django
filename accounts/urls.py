from django.urls import path
from . import views
from . import api
app_name ='accounts'
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('profile',views.user_profile,name='profile'),
    path('profile/jobs',views.user_posted_jobs,name='profile_jobs'),
    path('profile/job/owner/<int:pk>',views.job_posted_profile,name='job_posted_by'),
    path('profile/job/applicants/<int:pk>',views.job_applicants,name='job_applicants'),
    path('profile/edit',views.profile_edit,name='profile_edit'),
    
    
    #rest api 
    path('rest/profiles',api.FBV_Profile,name = "FBV_Profile"),
    
]
