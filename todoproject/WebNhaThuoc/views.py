# WebNhaThuoc/views.py
from django.shortcuts import render

def index(request):
    # Trả về trang chủ hoặc trang sản phẩm
    return render(request, 'WebNhaThuoc/index.html')
