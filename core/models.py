from django.db import models

# Create your models here.


class Contact(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    subject= models.CharField(max_length=50)
    text=models.TextField()
    def __str__(self):
         return self.name

class Projcts (models.Model):
    title=models.CharField(max_length=250)
    img=models.ImageField(upload_to='projects-img')
    link=models.CharField(max_length=250,blank=True,null=True)
     
