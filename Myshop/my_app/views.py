import re
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from store.models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

# my_app/templates/my_tmp/index.html
def trang_chu(request):    
    products = Product.objects.all().filter(is_available=True)
    context = {'products':products,}
    return render(request, 'my_tmp/index.html',context)
