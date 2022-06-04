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
    pay_type = models.CharField("pay type",choices=PAY_TYPE, default="alipay",max_length=10)
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
    """商品"""
    goods_code = models.CharField("number of goods", max_length=50, default="")
    name = models.CharField("商品名", max_length=100, )
    goods_num = models.IntegerField("库存数", default=0)
    market_price = models.FloatField("市场价格", default=0)
    shop_price = models.FloatField("本店价格", default=0)
    goods_brief = models.TextField("商品简短描述", max_length=500)

    ship_free = models.BooleanField("是否承担运费", default=True)
    # 首页中展示的商品封面图
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True,
    blank=True, verbose_name="封面图")
    # 首页中新品展示
    is_new = models.BooleanField("是否新品", default=False)
    # 商品详情页的热卖商品，自行设置
    is_hot = models.BooleanField("是否热销", default=False)
    add_time = models.DateTimeField("添加时间", default=datetime.now)
 
    # 商品分类:商品: 1:N
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE,
    verbose_name="商品类目")
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class GoodsImage(models.Model):
    """商品轮播图"""
    # 图片对象
    image = models.ImageField(upload_to="goods/images", verbose_name="图片",null=True, blank=True)
    add_time = models.DateTimeField("添加时间", default=datetime.now)
    # 商品：商品轮播图: 1:N
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", related_name="images")
    class Meta:
        verbose_name = '商品轮播'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.goods.name

