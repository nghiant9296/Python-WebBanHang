from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),  # Đường dẫn cho trang index
    path('product-detail/', views.product_detail, name='product-detail'),
    path('store/', views.store_page, name='store'),
    path('signin/', views.signin_page, name='signin'),
    path('register/', views.register_page, name='register'),
    path('cart/', views.cart_page, name='cart'),
    path('place-order/', views.place_order, name='place-order'),
]