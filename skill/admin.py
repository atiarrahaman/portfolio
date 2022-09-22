from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Skill)

class skillAdmin(admin.ModelAdmin):
    list_display=('id','title','width')
