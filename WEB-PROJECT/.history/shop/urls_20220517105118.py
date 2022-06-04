import imp
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop import views as shop_views
from .import views
routers = routers.SimpleRouter()

router.register(r'book', Clibrary_views.BookViewSets)
urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'login'),
]
