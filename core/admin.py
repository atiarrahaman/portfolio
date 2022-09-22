from django.contrib import admin

from  .models import *

# Register your models here.
@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','subject','text')
