from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from app_album_viewer.models import Album, UserProfile
from django.utils.translation import gettext as _
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
    if(request.method == 'POST'):
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
    return render(request, 'app_pages/account_view.html',context)

def rec_friend(request):
    context = {}
    id = request.GET.get('album')
    current_album = get_object_or_404(Album, pk=id)
    context["album"] = current_album
    context["trans_msgs"] = {   "rec_subject": _("RecommendEmailSubject"),
                                "rec_msg": _("RecommendEmailMessage") % {"album": current_album}}

    if request.user.is_authenticated:
        context["trans_msgs"]["rec_msg_user"] = _("RecommendEmailMessageWithUser") % {"album": current_album, "user": UserProfile.objects.get(user=request.user)}

    return render(request, 'app_pages/rec_friend_view.html',context)
