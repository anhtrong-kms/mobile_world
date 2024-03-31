from django.urls import path
from . import views

urlpatterns = [
    path('Store/', views.Store, name="Store")
]