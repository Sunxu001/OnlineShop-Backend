from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('shop/', include(router.urls))
    <--path('login/', views.LoginView.as_view(), name = 'login')
]
