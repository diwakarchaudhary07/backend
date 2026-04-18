from django.urls import path
from .views import home, show_products

urlpatterns = [
    path('', home, name='home'),                 #
    path('products/', show_products, name='products'),
]