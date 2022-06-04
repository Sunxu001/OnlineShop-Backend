from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from django.contrib.auth import login
from shop import models as shop_models
from .forms import LoginForm


# Create your views here.
class BrandViewSets(viewsets):
    queryset = shop_models.Brand
def home(request):
    return render(request, 'index.html')


