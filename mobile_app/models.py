from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from django.contrib.auth.forms import UserCreationForm
from django.db.models.lookups import IntegerFieldFloatRounding
from decimal import Decimal

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    sold_quantity = models.IntegerField(default=0)
    remaining_quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    origin = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def discounted_price(self):
        discount_amount = Decimal(self.price) * Decimal(self.discount) / Decimal(100)
        discounted_price = Decimal(self.price) - discount_amount
        return discounted_price
    def place_order(self, quantity):
        if quantity <= self.remaining_quantity:
            self.sold_quantity += quantity
            self.remaining_quantity -= quantity
            self.save()
            return True
        else:
            return False
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})  
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.address
class Resgister(UserCreationForm):
    user = models.CharField(max_length=255)
    email = models.EmailField()
    password1 = models.TextField(max_length=255)
    password2 = models.TextField(max_length=255)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class PrdouctGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)

    class Meta:
        verbose_name = 'Product gallery'
        verbose_name_plural = 'Product gallery'

    def __str__(self):
        return self.product.product_name
