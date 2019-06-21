from django.db import models

# Create your models here.
class Greeting(models.Model):
    ifsc = models.CharField(primary_key=True,max_length=255,blank=True)
    bank_id = models.CharField(max_length=255,blank=True)
    branch = models.CharField(max_length=255,blank=True)
    address = models.CharField(max_length=255,blank=True)
    city = models.CharField(max_length=255,blank=True)
    district = models.CharField(max_length=255,blank=True)
    state = models.CharField(max_length=255,blank=True)
    bank_name = models.CharField(max_length=255,blank=True)
