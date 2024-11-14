from django.shortcuts import render

def index(request):
    # Trả về trang chủ hoặc trang sản phẩm
    return render(request, 'NhaThuoc/index.html')

def product_detail(request):

    return render(request, 'NhaThuoc/product-detail.html')

def store_page(request):

    return render(request, 'NhaThuoc/store.html')

def signin_page(request):

    return render(request, 'NhaThuoc/signin.html')

def register_page(request):

    return render(request, 'NhaThuoc/register.html')

def cart_page(request):

    return render(request, 'NhaThuoc/cart.html')

def place_order(request):

    return render(request, 'NhaThuoc/place-order.html')