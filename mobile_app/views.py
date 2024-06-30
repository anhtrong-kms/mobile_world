from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests
from .models import Product
from django.contrib.auth import authenticate
#from .forms import RegistrationForm, UserForm, UserProfileForm

# Create your views here.
def Store(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
# Register
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(name=name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            # User Activation
            current_site = get_current_site(request)
            mail_subject = "Please activate your account!"
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })

            message = format_html(message)

            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Check your email to verify the account!')
            return redirect('login')

    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'login', context)
#  Login
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
def logout(request):
    auth.logout(request)
    messages.success(request, 'See you again')

    return redirect('base.html')
#Product
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product.html', {'product': product})
#Cart
def Cart(request):
    return render(request, 'cart.html', {})
#order
def Order(request,order_id):
    order_detail = OrderProduct.objects.filter(order__order_number=order_id)
    order = Order.objects.get(order_number=order_id)

    sub_total = 0

    for i in order_detail:
        sub_total += i.product_price * i.quantity

    context = {
        'order_detail': order_detail,
        'order': order,
        'sub_total': sub_total
    }
    return render(request, 'order.html', context)
def Checkout(request, total=0, quantity=0, cart_items=None):
    tax = 1
    grand_total = 0
    cart_items_count = 0

    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for car_item in cart_items:
            total += (car_item.product.price * car_item.quantity)
            quantity += car_item.quantity

        tax = (5 * total) / 100
        grand_total = total + tax

    except:
        pass

    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'grand_total': grand_total,
        'cart_items_count': cart_items_count,
    }

    return render(request, 'checkout.html', context)


def Phone(request):
    products = Product.objects.all()
    return render(request, 'phone.html', {'products': products})

def About(request):
    return reder(request,'about.html')

def Comment(request):
    return render(request,'comment.html')