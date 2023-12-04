from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name = "albums_index"),
    path('<int:id>', views.detail_view, name = "album_detail"),
    path('<int:id>/edit', views.edit_view, name = "album_edit"),
    path('new', views.create_view, name = "album_create"),
    path('<int:id>/songs', views.tracklist_view, name = "tracklist"),
    path('<int:a_id>/songs/<int:s_id>/', views.song_detail_view, name = "song_detail"),
]