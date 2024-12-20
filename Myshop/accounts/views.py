from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def signin_view(request):
    return render(request, 'my_tmp/signin.html')

def register(request):
    return render(request, 'my_tmp/register.html')
