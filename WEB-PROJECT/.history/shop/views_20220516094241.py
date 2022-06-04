from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views import View
from django.contrib.auth import login


# Create your views here.
def home(request):
    return render(request, 'index.html')

class LoginView(View):
    #login name of user
    def get (self, request):
        return render(request, 'login.html')