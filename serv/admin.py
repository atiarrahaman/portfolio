from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Service)
class serviceAdmin(admin.ModelAdmin):
    list_display=('id','title','text','img')
    
admin.site.register(Register)
