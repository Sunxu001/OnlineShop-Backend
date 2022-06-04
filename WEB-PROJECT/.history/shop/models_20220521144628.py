from termios import CREAD
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib

# Create your models here.
class Order(models.Model):
    CASH = 'cash'
    CRAD = 'card'
    PAYPAL = 'paypal'
    PAY_TYPE = (
        (CASH,"cash"),
        (CRAD, "card"),
        (PAYPAL,"paypal"),
    )
    family_name = models.CharField( max_length=50, blank=False, null=False)
    first_name = models.CharField( max_length=50, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=11, verbose_name="phone number", default="")
    address = models.CharField(max_length=200)
    quantity = models.IntegerField("Purchase quantity",default=0)
    pay_type = models.CharField("pay type",choices=PAY_TYPE, default="card",max_length=10)
    order_mount = models.FloatField("order mount",default=0.0)

def __str__(self):
    return f"{self.famliy_name} {self.first_name}"

class Login(models.Model):
    phone = models.CharField(max_length=11, verbose_name="phone number", default="")
    password = models.CharField(max_length=20)

def __str__(self):
    return f"{self.phone}"

class Subscription(models.Model):
    name = models.CharField( max_length=200, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=11, verbose_name="phone number", default="")
def __str__(self):
    return f"{self.email}"

class Goods(models.Model):
    goods_code = models.CharField("number of goods", max_length=50, default="")
    name = models.CharField("name of goods", max_length=100, )
    goods_num = models.IntegerField("Inventory (库存数)", default=0)
    market_price = models.FloatField("market price (市场价格)", default=0)
    shop_price = models.FloatField("shop price (本店价格)", default=0)
    goods_brief = models.TextField("Product short description (商品简短描述)", max_length=500)

    def __str__(self):
        return self.name


