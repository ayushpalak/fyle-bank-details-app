from django.conf import settings
from django.db import models
from django.utils import timezone


class bank_details(models.Model):
    ifsc = models.CharField(max_length=255)
    bank_id = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ifsc