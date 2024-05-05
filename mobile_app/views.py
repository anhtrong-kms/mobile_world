from django.shortcuts import render
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