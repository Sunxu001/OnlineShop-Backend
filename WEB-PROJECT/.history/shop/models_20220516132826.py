from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Order(models.Model):
    family_name = models.CharField( max_length=50, blank=False, null=False)
    first_name = models.CharField( max_length=50, blank=False, null=False)
    email = models.EmailField()
    mobile = models.CharField(max_length=11, verbose_name="phone number", default="")
    address = models.CharField(max_length=200)
    quantity = models.IntegerField("Purchase quantity",default=0)

def __str__(self):
    return f"{self.famliy_name} {self.first_name}"

class 