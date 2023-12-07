from django.test import TestCase, Client
from django.urls import reverse
from app_album_viewer.models import *
from django.contrib.auth.models import User

class TestAppPagesViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="password")
        self.user_profile = UserProfile.objects.create(user=self.user, display_name="Test User")
        self.album = Album.objects.create(title="Test Album")
        self.song = Song.objects.create(title="Test Song")
        self.album.song_set.add(self.song)
        self.comment = Comment.objects.create(user=self.user_profile, text="Test Comment", album=self.album)
        self.client = Client()
    
    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_account_view_not_logged_in(self):
        #check if user is redirected to login page if not logged in
        response = self.client.get(reverse("account"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))
        
        #check that the user will return to account_view after logging in
        next_url = reverse("account")
        next_parameter = f"?next={next_url}"
        self.assertContains(response, next_parameter)
    
    def test_account_view_logged_in(self):
        #check if username and comments are listed
        self.client.login(username="user", password="password")
        response = self.client.get(reverse("account"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        user_comments = self.user_profile.comment_set.all()
        for comment in user_comments:
            self.assertContains(response, comment.text)

    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 200)

    def test_rec_friend_view(self):
        response = self.client.get(reverse("rec_friend"))
        self.assertEqual(response.status_code, 200)