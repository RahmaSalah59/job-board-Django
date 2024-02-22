from django import forms
from .models import Apply ,job

class  ApplyForm(forms.ModelForm):

    class Meta:
        model = Apply
        fields = ['name','email','portfolio','cv','coverletter']
        

class AddJob(forms.ModelForm):
    class Meta:
        model = job
        fields = "__all__"
        exclude = ("owner","slug","profile_name")
    