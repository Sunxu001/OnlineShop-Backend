from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .import views
routers = routers.SimpleRouter()

router.registerr('')
urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'login'),
]
