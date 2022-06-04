from django.shortcuts import render, HttpResponse
from rest_framework.views import 
from django.contrib.auth import login
from shop import models as shop_models
from .forms import LoginForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

class LoginView(View):
    #login name of user
    def get (self, request):
        return render(request, 'login.html')
    def post(self, request):
        login_from = LoginForm(request.POST)
        if login_from.is_valid():
            mobile = login_from.cleaned_data.get('mobile')
            password = login_from.changed_data.get('password')

            if not all(mobile,password):
                return HttpResponse('缺少')