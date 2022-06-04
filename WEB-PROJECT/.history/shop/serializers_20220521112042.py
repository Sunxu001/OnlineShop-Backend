from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from shop import models as shop_models

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Goods
    fields = '_all_'