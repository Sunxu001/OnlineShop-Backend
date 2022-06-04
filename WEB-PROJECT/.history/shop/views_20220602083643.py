from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from shop import models as shop_models
from shop import serializers as shop_serializers




# Create your views here.
class GoodsViewSets(viewsets.ModelViewSet):
    queryset = shop_models.Goods.objects.all()
    serializer_class = shop_serializers.GoodsSerializer
   


def home_page(request):
    return render(request, 'index.html')

def new_page(request):
    return render(request, 'new.html')
    
def cloes_page(request):
    return render(request, 'cloes.html')

def login_page(request):
    f
    return render(request, 'login.html')

def message_page(request):
    return render(request, 'message.html')

def order_page(request):
    return render(request, 'order.html')

def pay_page(request):
    return render(request, 'pay.html')


