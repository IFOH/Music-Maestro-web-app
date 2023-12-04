from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . forms import *


def home(request):
    context = {}
    return render(request, 'app_pages/home_view.html',context)

def contact(request):
    context = {}
    return render(request, 'app_pages/contact_view.html',context)

def about(request):
    context = {}
    return render(request, 'app_pages/about_view.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('account')
    else:
        context = {}
        if(request.method == 'POST'):
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid login details")
        return render(request, 'app_pages/login_view.html',context)

def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required(login_url="login")
def account(request):
    context = {}
    return render(request, 'app_pages/account_view.html',context)
