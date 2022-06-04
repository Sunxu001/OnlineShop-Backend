from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views import View
from django.


# Create your views here.
def home(request):
    return render(request, 'index.html')

class LoginView(View)