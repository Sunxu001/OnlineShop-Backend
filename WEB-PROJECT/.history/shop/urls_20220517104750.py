from django.contrib import admin
from django.urls import path, include
from rest_framework imp
from .import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'login'),
]
