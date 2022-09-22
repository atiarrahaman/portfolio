from django.shortcuts import render ,HttpResponse, redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def home (request):

    context={'home':'active'}
    return render (request,  'home.html',context)

def contact (request):   
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        text=request.POST.get('text')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.text=text
        contact.save()
        return HttpResponse ("<h1 style='color: #2517ff;margin:50px;text-align:center'>Thanks For Your Contact </h1>")





    context={'contact':'active'}
    return render (request,  'contact.html',context)


def Login(request):
    if request.method== 'POST':
        fm= AuthenticationForm(data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            passw=fm.cleaned_data['password']
            user=authenticate(username=uname , password=passw)
            if user is not None:
                login(request,user)
                return redirect('/profile')
    else:
        fm= AuthenticationForm()
    context={'form':fm}
    return render(request,'login.html',context)

def Profile(request):
    if request.user.is_authenticated:
        
        return render(request,'profile.html')
    else:
        return redirect('/')

def Logout(request):
    logout(request)
    return redirect('/login')