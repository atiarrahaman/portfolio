from dataclasses import fields
from django import forms
from .models import Register

from django.contrib.auth.models import User


class registerForm(forms.ModelForm):
    class Meta:
        model= Register
        fields= ['name','blood_grp','phone']
        
        
class UserForm(forms.ModelForm):
    password1= forms.CharField( widget= forms.PasswordInput())
    password2= forms.CharField(label='Confirm Password', widget= forms.PasswordInput())
    class Meta:
        model= User
        fields = ['username',]