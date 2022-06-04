import imp
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop import views as shop_views
from .import views
router = routers.SimpleRouter()

router.register(r'book', shop_views.GoodsViewSets)

urlpatterns = [
    path('shop/', include()),
]
