from django.contrib import admin
from django.urls import path, include
from rest_framework
from .import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'login'),
]
