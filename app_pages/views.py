from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    context = {}
    return render(request, 'app_pages/login_view.html',context)

@login_required(login_url="login")
def account(request):
    context = {}
    return render(request, 'app_pages/account_view.html',context)
