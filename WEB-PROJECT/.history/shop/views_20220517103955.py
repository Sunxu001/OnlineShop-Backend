from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from django.contrib.auth import login
from shop import models as shop_models
from shop import serializers as shop_serializers
from .forms import LoginForm


# Create your views here.
class GoodsViewSets(viewsets):
    queryset = shop_models.Goods.objects.all()
    serializers = shop_serializers
def home(request):
    return render(request, 'index.html')


