from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from django.contrib.auth.forms import UserCreationForm
from django.db.models.lookups import IntegerFieldFloatRounding
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name

class Product(models.Model):  
    name = models.CharField(max_length=500)
    price = models.FloatField(default=15.5)
    image = models.ImageField()  

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

    