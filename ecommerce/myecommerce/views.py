from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
   return HttpResponse("Hello, Django!")

def category_products(request):
    categories = Category.objects.prefetch_related('products').all()
    return render(request, 'category_products.html', {'categories': categories})
