from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile


class signupfrom(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','password1','password2']

class profileform(forms.ModelForm):
    class Meta:
        model = profile
        exclude =('user',)

class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
