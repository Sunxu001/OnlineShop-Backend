from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from django.contrib.auth import login
from shop import models as shop_models
from shop import models as shop_models
from .forms import LoginForm


# Create your views here.
class GoodsViewSets(viewsets):
    queryset = shop_models.Goods.objects.all()
def home(request):
    return render(request, 'index.html')

