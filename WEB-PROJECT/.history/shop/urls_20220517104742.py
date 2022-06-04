from django.contrib import admin
from django.urls import path, include
from
from .import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'login'),
]
