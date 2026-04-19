from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# from collections import defaultdict

def home(request):
   return HttpResponse("Hello, Django!")


def show_products(request):
    products = Product.objects.all()   
    return render(request, 'products.html', {"products:products"})





















    # grouped_products = defaultdict(list)

    # for product in products:
        # grouped_products[product.category].append(product)

        # 'grouped_products': dict(grouped_products)