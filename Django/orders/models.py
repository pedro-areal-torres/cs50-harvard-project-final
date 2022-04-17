from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    orderNum=models.CharField(max_length=64,default='')    
    name=models.CharField(max_length=64)
    description=models.CharField(max_length=64)
    employer=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.orderNum} - {self.name} - {self.description} - {self.employer}"

class WorkOrder(models.Model):
    orderNum=models.CharField(max_length=64,default='')
    title=models.CharField(max_length=64)
    description=models.CharField(max_length=64)
    typeOrder=models.CharField(max_length=64)
    cost=models.CharField(max_length=64)
    createDate=models.CharField(max_length=64)
    startDate=models.CharField(max_length=64)
    endDate=models.CharField(max_length=64)
    priority=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} - {self.description} - {self.typeOrder} - {self.cost} - {self.createDate} - {self.startDate} - {self.endDate} - {self.priority}"