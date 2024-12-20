from django.db import models

class Shoes(models.Model):
    sId=models.AutoField(primary_key=True)
    sName=models.CharField(max_length=100)
    sbrand=models.CharField(max_length=100)
    size=models.IntegerField()
    stype=models.CharField(max_length=100)
    price=models.FloatField(default=0.0)
    STATUS_CHOICES=[
        ('Men','men'),
        ('Women','women'),
        ('Girls','girls'),
        ('Boys','boys'),
    ]
    
    status=models.CharField(max_length=10, choices=STATUS_CHOICES,default='active')
# Create your models here.
