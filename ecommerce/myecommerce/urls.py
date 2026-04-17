from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    path('categorie', category_products, name='category_products'),
]
