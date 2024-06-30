from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.urls import reverse
import uuid
from django.contrib.auth.forms import UserCreationForm
from django.db.models.lookups import IntegerFieldFloatRounding
from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist

#
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user', 'name', 'phone']
    def __str__(self):
        return self.name

#THỂ LOẠI HÀNG
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#MẶT HÀNG
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

#Địa Chỉ khách hàng
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(blank ="True",max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(blank=True, max_length=20)
    
    # profile_picture = models.ImageField(blank=True, null=True, upload_to='userprofile')

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address}'

    def get_user(self):
        try:
            return self.user
        except ObjectDoesNotExist:
            return None
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
    def __str__(self):
        return self.user
class Login(BaseUserManager):
    # create normal user
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('User must have an email!')

        if not username:
            raise ValueError('User must have an username!')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # create super user
    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class PrdouctGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)

    class Meta:
        verbose_name = 'Product gallery'
        verbose_name_plural = 'Product gallery'

    def __str__(self):
        return self.product.product_name
