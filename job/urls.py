from django.urls import path
from . import views



urlpatterns = [
    path('',views.all_jobs,name='all_jobs'),
    path('/<int:pk>', views.job_details,name='job_details'),

]
