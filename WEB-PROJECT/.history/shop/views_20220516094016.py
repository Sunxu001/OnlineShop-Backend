from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, 'index.html')

class LoginView()