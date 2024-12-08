from django.urls import path
from . import views

urlpatterns = [
    path('', views.trang_chu, name="index"),         
    path('trang-chu', views.trang_chu, name="index"),  #.html    
]