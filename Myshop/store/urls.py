from django.urls import path
from . import views

urlpatterns = [  
    path('', views.kho_hang, name="store"),  #.html
    path('category/<slug:category_slug>/',views.kho_hang,name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',views.chi_tiet_san_pham,
                name='product_detail'),
    path('search/', views.tim_kiem_san_pham,name='search'),    
]