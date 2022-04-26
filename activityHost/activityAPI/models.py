from django.db import models

# Create your models here.

class Master(models.Model):

    industry = models.CharField(max_length=50)
    oppNumber = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    prodCode = models.CharField(max_length=6)
    request = models.CharField(max_length=25)
    sales = models.CharField(max_length=25)
    projManager = models.CharField(max_length=25)
    engineer = models.CharField(max_length=25)
    reqDate = models.DateField(auto_now=False, auto_now_add=True)
    dueDate = models.DateField(auto_now=False, auto_now_add=True)
    compDate = models.DateField(auto_now=False, auto_now_add=True)
    comments = models.CharField(max_length=1000)
    reqDate.editable = True
    dueDate.editable = True
    compDate.editable = True