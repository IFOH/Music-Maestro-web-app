from django.test import TestCase, Client
from django.urls import reverse
from .models import *

class TestAlbumViewerViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="password")
        self.user_profile = UserProfile.objects.create(user=self.user, display_name="Test User")
        self.album = Album.objects.create(title="Test Album")
        self.song = Song.objects.create(title="Test Song")
        self.album.song_set.add(self.song)
        self.comment = Comment.objects.create(user=self.user_profile, text="Test Comment", album=self.album)
        self.client = Client()

    def test_index_view(self):
        #check if album is listed
        response = self.client.get(reverse("albums_index"))
        self.assertEqual(response.status_code, 200)
        album_list = response.context["album_list"]
        self.assertIn(self.album,album_list)

    def test_detail_view(self):
        #check if comments are listed
        response = self.client.get(reverse("album_detail", args=[self.album.id]))
        self.assertEqual(response.status_code, 200)
        comment_list = response.context["comment_list"]
        self.assertIn(self.comment,comment_list)

    def test_edit_view_UPDATE(self):
        #check if album can be updated
        url = reverse("album_edit", args=[self.album.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        post_data = {
            "title": "Updated Album Title",
            "update_album": ""
        }
        response_post = self.client.post(url, post_data, follow=True)
        self.assertEqual(response_post.status_code, 200)

        updated_album = Album.objects.get(id=self.album.id)
        self.assertEqual(updated_album.title, "Updated Album Title")

    def test_edit_view_DELETE(self):
        #check if album can be deleted
        url = reverse("album_edit", args=[self.album.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        post_data = {
            "delete_album": ""
        }
        response_post = self.client.post(url, post_data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        try:
            album = Album.objects.get(id=self.album.id)
        except Album.DoesNotExist:
            album = None
        self.assertIsNone(album)

    def test_edit_view_songs(self):
        #check if songs can be added and removed from albums
        url = reverse("album_edit", args=[self.album.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        def toggle_add_remove():
            post_data = {
                "song_choice": self.song.title,
                "update_song": ""
            }
            response_post = self.client.post(url, post_data, follow=True)
            self.assertEqual(response_post.status_code, 200)

        toggle_add_remove() #song removed from album
        self.assertFalse(self.album.song_set.filter(title=self.song.title).exists())
        toggle_add_remove() #song added to album
        self.assertTrue(self.album.song_set.filter(title=self.song.title).exists())

    def test_create_view(self):
        #check if albums can be created
        response = self.client.get(reverse("album_create"))
        self.assertEqual(response.status_code, 200)
        create_data = {
            "title": "New Album"
        }
        response = self.client.post(reverse("album_create"), create_data)
        self.assertEqual(response.status_code, 302)  #successful redirect
        self.assertTrue(Album.objects.filter(title="New Album").exists())

        #check invalid data
        create_data = {
            "description": "New Album Description"
        }
        response = self.client.post(reverse("album_create"), create_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")

    def test_tracklist_view(self):
        #check if songs are listed
        response = self.client.get(reverse("tracklist", args=[self.album.id]))
        self.assertEqual(response.status_code, 200)
        song_list = response.context["song_list"]
        self.assertIn(self.song,song_list)

    def test_song_detail_view(self):
        #check if the correct song and album are listed
        response = self.client.get(reverse("song_detail", args=[self.album.id, self.song.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.song,response.context["song"])
        self.assertEqual(self.album,response.context["album"])