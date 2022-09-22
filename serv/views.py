from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def Singup(request):
      fm=UserForm()
      form=registerForm()
      context={'fm':fm ,'form':form}
      return render( request,'register.html',context)
    # Constration ,edit 28-1-2022
def service(request):
    service= Service.objects.all()


    context={
    'service':'active',
      'ser':service
    
    }
    return render (request  ,'service.html',context)
