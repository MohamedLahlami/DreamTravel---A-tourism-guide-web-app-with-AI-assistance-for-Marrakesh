from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    return redirect('login')

