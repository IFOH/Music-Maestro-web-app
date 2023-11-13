from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    context = {}
    return render(request, 'app_pages/home.html',context)

def contact(request):
    context = {}
    return render(request, 'app_pages/contact.html',context)

def account(request):
    context = {}
    return HttpResponse("account")