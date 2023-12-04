from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
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
        form = LoginForm(request.POST or None)
        if(request.method == 'POST'):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                if not User.objects.filter(username=username).exists():
                    messages.error(request, "User does not exist")
                else:
                    form.fields['username'].initial = username
                    messages.error(request, "Incorrect password")
        context["form"] = form
        return render(request, 'app_pages/login_view.html',context)

def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required(login_url="login")
def account(request):
    context = {}
    return render(request, 'app_pages/account_view.html',context)
