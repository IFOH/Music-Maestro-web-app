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
    album_comments = Comment.objects.filter(album=current_album)
    context["comment_list"] = album_comments
    context["album"] = current_album
    return render(request, 'app_album_viewer/detail_view.html', context)

def edit_view(request, id):
    context = {}
    current_album = get_object_or_404(Album, pk=id)
    album_form = AlbumForm(request.POST or None, instance=current_album)
    
    if(request.method == 'POST'):
        #Edit album model
        if "update_album" in request.POST:
            if album_form.is_valid():
                album_form.save()
                messages.success(request, "Album updated successfully")
        #Delete album
        elif "delete_album" in request.POST:
            current_album.delete()
            return redirect('albums_index')
        #Add and remove songs from album
        elif "update_song" in request.POST:
            song_to_update = get_object_or_404(Song, title=request.POST.get("song_choice"))
            if song_to_update in current_album.song_set.all():
                current_album.song_set.remove(song_to_update)
                messages.success(request, "Song removed")
            else:
                current_album.song_set.add(song_to_update)
                messages.success(request, "Song added")
            return redirect(reverse('album_edit', args=[id]))

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

def song_detail_view(request, a_id, s_id):
    context = {}
    current_album = get_object_or_404(Album, pk=a_id)
    current_song = get_object_or_404(Song, pk=s_id)
    context["song"] = current_song
    context["album"] = current_album
    return render(request, 'app_album_viewer/song_detail_view.html', context)

def tracklist_view(request, id):
    context = {}
    current_album = get_object_or_404(Album, pk=id)
    album_songs = Song.objects.filter(album=current_album)
    context["song_list"] = album_songs
    context["album"] = current_album
    return render(request, 'app_album_viewer/tracklist_view.html', context)

def create_view(request):
    context = {}
    form = AlbumForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            form.save()
            return redirect('albums_index')
    
    context["form"] = form
    return render(request, 'app_album_viewer/create_view.html', context)