from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    
    mobile = models.CharField(max_length=11, verbose_name="手机", default="")