from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
   return HttpResponse("Hello, Django!")

def show_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})