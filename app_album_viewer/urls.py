from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name = "albums_index"),
    path('<int:id>', views.detail_view, name = "album_detail"),
    path('<int:id>/edit', views.edit_view, name = "album_edit"),
]