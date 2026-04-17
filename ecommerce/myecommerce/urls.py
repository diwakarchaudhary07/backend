from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    path('products', show_products, name='show_products'),
]
