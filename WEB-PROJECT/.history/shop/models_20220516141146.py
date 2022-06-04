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


class GoodsCategory(models.Model):
    """商品分类"""
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField('类别名', default="", max_length=30, help_text="类别名")
    code = models.CharField("类别code", default="", max_length=30, help_text="类别code")
    desc = models.TextField("类别描述", default="", help_text="类别描述")
    # 目录树级别
    category_type = models.IntegerField("类目级别", choices=CATEGORY_TYPE,help_text="类目级别")
# 一级分类: 电器 二级分类: 微波炉、电磁炉...
# 一级分类：二级分类 = 1:N
# 设置models有一个指向自己的外键
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE,null=True, blank=True, verbose_name="父类目级别",help_text="父目录",related_name="sub_cat")
    is_tab = models.BooleanField("是否导航", default=False, help_text="是否导航")
    add_time = models.DateTimeField("添加时间", default=datetime.now)
    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

————————————————
版权声明：本文为CSDN博主「浅浅~Smile」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/daidadeguaiguai/article/details/105324030
class Goods(models.Model):
    """商品"""
    goods_code = models.CharField("number of goods", max_length=50, default="")
    name = models.CharField("商品名", max_length=100, )
    goods_num = models.IntegerField("库存数", default=0)
    market_price = models.FloatField("市场价格", default=0)
    shop_price = models.FloatField("本店价格", default=0)
    goods_brief = models.TextField("商品简短描述", max_length=500)
    # 商品分类:商品: 1:N
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE,
    verbose_name="商品类目")
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


