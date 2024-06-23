from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests
from .models import Product
from django.contrib.auth import authenticate

# Create your views here.
def Store(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email = email ,password = password)
        if user is not None :
            current_user = Account.objects.filter(email=email).first()
            is_admin = current_user.is_admin
            if is_admin is True:
                auth.login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('admin-index')
            elif is_admin is False:
                try:
                    cart = Cart.objects.get(cart_id=_cart_id(request))
                    is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                    if is_cart_item_exists:
                        cart_item = CartItem.objects.filter(cart=cart)
                        for item in cart_item:
                            item.user = user
                            item.save()
                except:
                    pass
                auth.login(request, user)
                messages.success(request, 'Logged in successfully!')
                url = request.META.get('HTTP_REFERER')
                try:
                    query = requests.utils.urlparse(url).query
                    params = dict(x.split('=') for x in query.split('&'))

                    if 'next' in params:
                        nextPage = params['next']

                        return redirect(nextPage)
                except:
                    return redirect('Store')
        else:
            messages.error(request, 'Email or password is incorrect!')
            return redirect('login')
    return render(request, 'login.html', {})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    product_gallery = PrdouctGallery.objects.filter(product_id=single_product.id)
    return render(request, 'product.html', {'product': product})

def Cart(request):
    return render(request, 'cart.html', {})

def Checkout(request):
    return render(request, 'checkout.html', {})

def Order(request):
    return render(request, 'order.html', {})