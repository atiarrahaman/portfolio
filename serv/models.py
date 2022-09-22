import profile
from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
# Create your models here.



class Service(models.Model):
    img =models.ImageField(upload_to='ser_image')
    title=models.CharField( max_length=50)
    text=models.TextField(max_length=1000)


class Register(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    blood_grp = models.CharField(max_length=50)
    phone= models.IntegerField()