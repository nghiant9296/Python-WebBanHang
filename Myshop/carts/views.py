from difflib import Match
import math
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from carts.models import Cart, CartItem
from django.http import HttpResponse

# fix bug
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def _thong_tin_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def them_vao_gio_hang(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id = _thong_tin_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _thong_tin_cart_id(request))
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')
    # return HttpResponse(cart_item.quantity)

def gio_hang(request, total=0, quantity=0,cart_items=None):
    tax = 0
    grand_total = 0
    try:
        cart = Cart.objects.get(cart_id = _thong_tin_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active = True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        # xử lý tax và grand total (tax = 8%, grand_total = total * 1.08)
        tax = (total*8)/100
        grand_total = round(total*1.08,2)
    # fix
    except ObjectDoesNotExist:
        pass
    data = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total': grand_total
    }
    return render(request, 'my_tmp/cart.html',context=data)

# Nghiệp vụ giảm bớt sản phẩm trong giỏ hàng
def giam_san_pham(request, product_id):
    cart = Cart.objects.get(cart_id = _thong_tin_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

# Nghiệp vụ xóa sản phẩm khỏi giỏ hàng
def xoa_san_pham(request, product_id):
    cart = Cart.objects.get(cart_id = _thong_tin_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')