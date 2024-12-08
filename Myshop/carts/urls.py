from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8080/cart/
    path('', views.gio_hang, name='cart'),
    path('add_cart/<int:product_id>/',views.them_vao_gio_hang, name='add_cart'),
    path('decrement_cart/<int:product_id>/',views.giam_san_pham, name='decrement_cart'),
    path('remove_item_cart/<int:product_id>/',views.xoa_san_pham, name='remove_item_cart')
]
