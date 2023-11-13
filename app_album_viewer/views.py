from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *

def index_view(request):
    context = {}
    context["album_list"] = Album.objects.all()
    return render(request, 'app_album_viewer/index_view.html',context)

def detail_view(request, id):
    context = {}
    current_album = get_object_or_404(Album, pk=id)
    context["album"] = current_album
    album_songs = Song.objects.filter(album=current_album)
    context["songs"] = album_songs
    return render(request, 'app_album_viewer/detail_view.html', context)

def edit_view(request, id):
    context = {}
    current_album = get_object_or_404(Album, pk=id)
    context["current_songs"] = Song.objects.filter(album=current_album)
    context["missing_songs"] = Song.objects.exclude(album=current_album)
    return render(request, 'app_album_viewer/edit_view.html', context)