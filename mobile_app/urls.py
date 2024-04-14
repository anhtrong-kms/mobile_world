from django.urls import path
from . import views
from .views import update_products_from_api

urlpatterns = [
    path('', views.Store, name="Store"),
    path('login/', views.Login, name="Login"),
    path('register/', views.Register, name="Register"),
    path('update-products/', update_products_from_api, name='update_products'),
]
