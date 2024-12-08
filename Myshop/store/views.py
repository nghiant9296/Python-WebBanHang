from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from carts.models import CartItem
from category.models import Category
from store.models import Product

from carts.views import _thong_tin_cart_id
from carts.models import CartItem

# thêm thư viện cho phân trang sản phẩm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
# my_app/templates/my_tmp/store.html
def kho_hang(request, category_slug=None):
    categories = None
    products = None    
    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        # phân trang sản phẩm
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
            
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        # phân trang sản phẩm
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
        product_count = products.count()       
    data = {'products':paged_products, 
            'product_count':product_count
    }    
    return render(request, 'my_tmp/store.html',context=data)

# my_app/templates/my_tmp/product-detail.html
def chi_tiet_san_pham(request, category_slug, product_slug):
    try:
        # category is ForeignKey() -> Category: slug -> Syntax: category__slug 
        single_product = Product.objects.get(
                category__slug = category_slug, slug = product_slug)
        # Kiểm tra sản phẩm có tồn tại trong giỏ hàng?
        # cart is ForeignKey
        in_cart = CartItem.objects.filter(cart__cart_id=_thong_tin_cart_id(request), 
                        product=single_product).exists()
        # return HTTPResponse(in_cart)
    except Exception as e:
        raise e
    data = {'single_product':single_product,
            'in_cart':in_cart,}
    return render(request, 'my_tmp/product-detail.html', context=data)

def tim_kiem_san_pham(request):   
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(product_name__icontains=keyword)
            paginator = Paginator(products, 6)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)
        else:
            products = Product.objects.all().filter(is_available=True)
            # phân trang sản phẩm
            paginator = Paginator(products, 6)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)        
            product_count = products.count()
    data = {
        'products':paged_products,
    }    
    return render(request, 'my_tmp/store.html', context=data)