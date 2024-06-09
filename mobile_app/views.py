from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests
from .models import Product

# Create your views here.
def Store(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def Login(request):
    return render(request, 'login.html', {})

def Register(request):
    return render(request, 'register.html', {})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product.html', {'product': product})

def Cart(request):
    return render(request, 'cart.html', {})

def Checkout(request):
    return render(request, 'checkout.html', {})

def Order(request):
    return render(request, 'order.html', {})