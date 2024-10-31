# WebNhaThuoc/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Đường dẫn cho trang index
]
