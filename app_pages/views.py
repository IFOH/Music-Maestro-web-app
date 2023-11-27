from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    context = {}
    return render(request, 'app_pages/home.html',context)

def contact(request):
    context = {}
    return render(request, 'app_pages/contact.html',context)

def about(request):
    context = {}
    return render(request, 'app_pages/about.html',context)

def login(request):
    context = {}
    return render(request, 'app_pages/login.html',context)

def account(request):
    context = {}
    return HttpResponse("account")