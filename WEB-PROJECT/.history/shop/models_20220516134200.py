from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib

# Create your models here.
class Order(models.Model):
    PAY_TYPE = (
        ("cash"),
        ("card"),
        ("paypal"),
    )
    family_name = models.CharField( max_length=50, blank=False, null=False)
    first_name = models.CharField( max_length=50, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=11, verbose_name="phone number", default="")
    address = models.CharField(max_length=200)
    quantity = models.IntegerField("Purchase quantity",default=0)
    pay_type = models.CharField("pay ",choices=PAY_TYPE, default="alipay",max_length=10)
    order_mount = models.FloatField("订单金额",default=0.0)

def __str__(self):
    return f"{self.famliy_name} {self.first_name}"

class Login(models.Model):
    phone = models.CharField(max_length=11, verbose_name="phone number", default="")
    password = models.CharField(max_length=20)

def __str__(self):
    return f"{self.phone}"

class 
