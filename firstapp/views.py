from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'home/index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'home/product_list.html', {'products': products})