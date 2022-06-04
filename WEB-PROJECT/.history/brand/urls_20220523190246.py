"""brand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django import urls
from pathlib import Path

from django.urls import path, include
from shop.views import home_page,new_page,cloes_page,login_page,message_page,order_page,pay_page
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls'), name="api"),
    path('', home_page, name="home"),
    path('new/',new_page, name="new"),
    path('cloes/',cloes_page, name="cloes"),
    path('login/',login_page, name="login"),
    path('message/',message_page, name="message"),
    path('order/',order_page, name="order"),
    path('pay/',pay_page, name="pay"),


]+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
