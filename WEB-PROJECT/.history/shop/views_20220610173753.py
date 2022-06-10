from itertools import product
from django.shortcuts import render, HttpResponse, redirect
from rest_framework import viewsets
from shop import models as shop_models
from shop import serializers as shop_serializers
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Goods, Login, Subscription, Order
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class GoodsViewSets(viewsets.ModelViewSet):
    queryset = shop_models.Goods.objects.all()
    serializer_class = shop_serializers.GoodsSerializer


def home_page(request):
    products = Goods.objects.all()[:5]
    user_phone = request.COOKIES.get('phone')
    if not user_phone:
        user_phone = 'NoLogin'
    return render(request, 'index.html', {'products': products, 'user_phone': user_phone})


def new_page(request):
    products = Goods.objects.all()
    return render(request, 'new.html', {'products': products})


def cloes_page(request, goods_code):
    product = Goods.objects.filter(goods_code=goods_code).first()
    return render(request, 'cloes.html', {'product': product})


def login_page(request):
    if request.method == "POST":
        password = request.POST.get('Password')
        phone = request.POST.get('Phone')
        print(phone, '   ', password)
        user = Login.objects.filter(phone=phone)
        if user.exists():
            user = user.first()
            resp = redirect('/')
            resp.set_cookie('phone', user.phone)
            return resp

        user = Login.objects.create(phone=phone, password=password)
        resp = redirect('/')
        resp.set_cookie('phone', user.phone)
        return resp
    return render(request, 'login.html')


def message_page(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        Subscription.objects.create(name=name, email=email, phone=phone)
        return redirect('/message')
    return render(request, 'message.html')


def order_page(request):
    if request.method == "POST":
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        paymethod = request.POST.get('paymethod')
        Order.objects.create(last_name=last_name, family_name=first_name, phone=phone, address=address,
                             quantity=quantity, pay_type=paymethod)
        return redirect('/')
    return render(request, 'order.html')


def regiter_page(request):
    return render(request, 'regiter.html')
