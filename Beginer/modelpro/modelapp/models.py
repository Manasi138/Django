from django.db import models

# Create your models here.
#Object Relational Mapping

class Employee(models.Model):
    empName=models.CharField(max_length=100)
    empsalary=models.FloatField(default=0.0)
    designation=models.CharField(max_length=100)