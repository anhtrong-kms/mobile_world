from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store, name="Store"),
    path('login/', views.login, name="login"),
    path('product/<int:id>',views.product_detail,name='product'),
    path('cart/', views.Cart, name="Cart"),
    path('checkout/', views.Checkout, name="Checkout"),
    path('order/', views.Order, name="Order"),
    path('category/<slug:category_slug>/<product_slug>/', views.product_detail, name='product_detail'),
]
    