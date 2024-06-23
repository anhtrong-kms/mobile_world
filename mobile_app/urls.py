from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store, name="Store"),
    path('login/', views.login, name="login"),
    path('product/<int:id>',views.product_detail,name='product'),
    path('cart/', views.Cart, name="Cart"),
    path('checkout/', views.Checkout, name="Checkout"),
    path('order/', views.Order, name="Order"),
<<<<<<< HEAD
    path('category/<slug:category_slug>/<product_slug>/', views.product_detail, name='product_detail'),
=======
    path('phone/', views.Phone, name="Phone"),
>>>>>>> af16f8e66dfd2f9dfb90463b2031fc2840f7c896
]
    