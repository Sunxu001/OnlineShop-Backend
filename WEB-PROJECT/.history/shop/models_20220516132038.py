from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class O(models.Model):
    family_name = models.CharField( max_length=50, blank=False, null=False)
    first_name = models.CharField( max_length=50, blank=False, null=False)
    email = models.EmailField()
    mobile = models.CharField(max_length=11, verbose_name="phone number", default="")
    address = models.CharField(max_length=200)