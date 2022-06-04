from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop import views as Clibrary_views
router =  routers.SimpleRouter()

urlpatterns = [
    path('shop/', include(router.urls)),
    path('login/', views.LoginView.as_view(), name = 'login'),
]
