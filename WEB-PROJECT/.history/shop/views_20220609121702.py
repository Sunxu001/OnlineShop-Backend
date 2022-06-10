from itertools import product
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from shop import models as shop_models
from shop import serializers as shop_serializers
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Goods, Login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class GoodsViewSets(viewsets.ModelViewSet):
    queryset = shop_models.Goods.objects.all()
    serializer_class = shop_serializers.GoodsSerializer
   


def home_page(request):
    products = Goods.objects.all()
    return render(request, 'index.html', {'products':products})

def new_page(request):
    products = Goods.objects.all()
    return render(request, 'new.html',{'products':products})
    
def cloes_page(request, goods_code):
    product = Goods.objects.filter(goods_code = goods_code).first()
    return render(request, 'cloes.html', {'product':product})

def login_page(request):
        form = Login.User.objects.filter(PHONE=Phone, PASSWORD=Password)
        Phone = request.POST['PHONE']
        Password = request.POST['PASSWORD']
        Login.objects.create(PHONE=Phone, PASSWORD=Password)
        return render(request, 'login.html', {'PHONE': Phone, 'PASSWORD': Password})

def message_page(request):

    return render(request, 'message.html')

def order_page(request):

    return render(request, 'order.html')

def regiter_page(request):

    return render(request, 'regiter.html')


