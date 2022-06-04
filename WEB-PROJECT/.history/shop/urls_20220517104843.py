from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .import views
routers = r
urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'login'),
]
