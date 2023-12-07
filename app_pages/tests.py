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

    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_account_view_not_logged_in(self):
        #check if user is redirected to login page if not logged in
        response = self.client.get(reverse("account"), follow=True)
        self.assertEqual(response.status_code, 200)
        next_url = "?next=" + reverse("account")
        self.assertRedirects(response, reverse("login") + next_url)
    
    def test_account_view_logged_in(self):
        #check if username and comments are listed
        self.client.login(username=self.user.username, password="password")
        response = self.client.get(reverse("account"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        user_comments = self.user_profile.comment_set.all()
        for comment in user_comments:
            self.assertContains(response, comment.text)

    def test_login_view_logged_in(self):
        #check if user is redirected to account if already logged in
        self.client.login(username=self.user.username, password="password")
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account"))

    def test_login_view_with_valid_login(self):
        #check if user can login with correct credentials
        login_data = {
            "username": self.user.username,
            "password": "password"
        }
        response = self.client.post(reverse("login"), login_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_with_invalid_user(self):
        #check login with incorrect user
        login_data = {
            "username": "Invalid User",
            "password": "Invalid Password"
        }
        response = self.client.post(reverse("login"), login_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertContains(response, "User does not exist")

    def test_login_view_with_invalid_password(self):
        #check login with incorrect password
        login_data = {
            "username": self.user.username,
            "password": "Invalid Password"
        }
        response = self.client.post(reverse("login"), login_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertContains(response, "Incorrect password")

    def test_logout_view(self):
        #check if a logged in user is successfully logged out
        self.client.login(username=self.user.username, password="password")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_rec_friend_view_logged_out(self):
        #check if user is redirected to login page if not logged in
        response = self.client.get(reverse("rec_friend"), follow=True)
        self.assertEqual(response.status_code, 200)
        next_url = "?next=" + reverse("rec_friend")
        self.assertRedirects(response, reverse("login") + next_url)

    def test_rec_friend_view_logged_in(self):
        #check if album is recommended
        url = reverse("rec_friend") + "?album=" + str(self.album.id)
        self.client.login(username=self.user.username, password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.album,response.context["album"])

        #check if an email can be correctly sent
        post_data = {
            "recipient_email": "example@email.com",
            "subject": "Subject",
            "message": "Message",
            'album': self.album.id
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("album_detail", args=[self.album.id]))