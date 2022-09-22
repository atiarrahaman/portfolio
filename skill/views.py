from django.shortcuts import render
from .models import *

# Create your views here.
def skill(request):
    skill=Skill.objects.all()


    context={
     'skill':'active',
     'sk':skill
        
        }
    return render(request,'skill.html',context)