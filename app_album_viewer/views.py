from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import *
from .forms import *

def index_view(request):
    context = {}
    context["album_list"] = Album.objects.all()
    return render(request, 'app_album_viewer/index_view.html',context)

def detail_view(request, id):
    context = {}
    current_album = get_object_or_404(Album, pk=id)
    album_songs = Song.objects.filter(album=current_album)
    album_comments = Comment.objects.filter(album=current_album)
    context["song_list"] = album_songs
    context["comment_list"] = album_comments
    context["album"] = current_album
    return render(request, 'app_album_viewer/detail_view.html', context)

def edit_view(request, id):
    context = {}
    current_album = get_object_or_404(Album, pk=id)
    #Edit album model
    album_form = AlbumForm(request.POST or None)

    #Add and remove songs from album
    if(request.method == 'POST'):
        song_to_update = get_object_or_404(Song, title=request.POST.get("song_choice"))
        if song_to_update in current_album.song_set.all():
            current_album.song_set.remove(song_to_update)
            messages.success(request, "Song removed")
        else:
            current_album.song_set.add(song_to_update)
            messages.success(request, "Song added")
        return redirect('album_edit', id=id)

    #Context dictionary
    song_list = []
    for song in Song.objects.all():
        if current_album.song_set.contains(song):
            song_list.append({"obj":song, "in_album":True})
        else:
            song_list.append({"obj":song, "in_album":False})
    
    context["song_list"] = song_list
    context["album"] = current_album
    context["album_form"] = album_form
    return render(request, 'app_album_viewer/edit_view.html', context)


def create_view(request):
    context = {}
    form = AlbumForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            form.save()
            return redirect('albums_index')
    else:
        context["form"] = form
        return render(request, "app_album_viewer/create_view.html", context)