from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from app_album_viewer.models import Album
from django.utils.translation import gettext as _
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
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
    
    context = {}
    form = LoginForm(request.POST or None)
    if(request.method == "POST"):
        if form.is_valid():
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
                    messages.error(request, "Incorrect password")
            form.fields['username'].initial = username
    context["form"] = form
    return render(request, 'app_pages/login_view.html',context)

def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required(login_url="login")
def account(request):
    context = {}
    context["comment_list"] = request.user.userprofile.comment_set.all()
    return render(request, 'app_pages/account_view.html',context)

@login_required(login_url="login")
def rec_friend(request):
    context = {}
    id = request.GET.get("album")
    current_album = get_object_or_404(Album, pk=id)
    form = EmailForm(request.POST or None)
    form.initial["subject"] = _("RecommendEmailSubject")
    form.initial["message"] = _("RecommendEmailMessage") % {"album": current_album}

    if(request.method == 'POST'):
        if form.is_valid():
            recipient_email = form.cleaned_data["recipient_email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject=subject,message=message,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=[recipient_email])
                messages.success(request, "Email sent")
                return redirect('album_detail', id=id)
            except BadHeaderError:
                messages.error(request, "Invalid characters")

    context["form"] = form
    context["album"] = current_album
    
    return render(request, 'app_pages/rec_friend_view.html',context)

