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

def update_products_from_api(request):
    # Gửi yêu cầu GET đến API và lấy dữ liệu
    response = requests.get('https://fakestoreapi.com/products')
    
    if response.status_code == 200:
        products_data = response.json()  # Chuyển đổi dữ liệu nhận được sang định dạng JSON
        for product_data in products_data:
            # Tạo hoặc cập nhật sản phẩm trong cơ sở dữ liệu Django từ dữ liệu nhận được từ API
            product, created = Product.objects.update_or_create(
                id=product_data['id'],
                defaults={
                    'name': product_data['title'],
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'category': product_data['category'],
                    'image': product_data['image'],
                    # Thêm các trường khác của model Product nếu cần
                }
            )
            # Update sold_quantity và remaining_quantity tương ứng
            product.remaining_quantity = product_data.get('quantity', 0)
            product.sold_quantity = product_data.get('quantity', 0) - product.remaining_quantity
            product.save()
            
        message = "Dữ liệu đã được cập nhật từ API thành công."
    else:
        message = "Không thể lấy dữ liệu từ API."
    
    return HttpResponse(message)