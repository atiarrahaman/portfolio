from django.db import models

# Create your models here.

class Skill(models.Model):
    title= models.CharField( max_length=50)
    p_parcent= models.CharField( max_length=50)
    width= models.CharField( max_length=50)
    color= models.CharField( max_length=50)
