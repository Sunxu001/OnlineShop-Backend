from pyexpat import model
from rest_framework import serializers
from shop import models as shop_models

class GoodsSerializer(serializers.ModelSerializer):
    model = shop_models.Goods
    fir