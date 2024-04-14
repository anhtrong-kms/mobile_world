from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Product

# Create your views here.
def Store(request):
    return render(request, 'index.html', {})

def Login(request):
    return render(request, 'login.html', {})

def Register(request):
    return render(request, 'register.html', {})