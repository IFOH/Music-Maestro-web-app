from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from .forms import AlbumForm

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
    if(request.method == 'POST'):
        #GET FORM DATA AND UPDATE ALBUM
        return redirect('album_detail', id=id)

    songs = []
    for song in Song.objects.all():
        if song.album == current_album:
            songs.append({"obj":song, "in_album":True})
        else:
            songs.append({"obj":song, "in_album":False})
    
    context["songs"] = songs
    return render(request, 'app_album_viewer/edit_view.html', context)


def create_view(request):
    context = {}
    form = AlbumForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            form.save()
            return redirect('albums_index')
    else:
        context['form'] = form
        return render(request, "app_album_viewer/create_view.html", context)