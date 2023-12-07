from django.core.management.base import BaseCommand
from app_album_viewer.models import *
from datetime import datetime
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Resetting database")
        clear_data()
        sample_file = open("sample_data/sample_data.json")
        sample_data = json.load(sample_file)
        self.stdout.write("Seeding data")
        if ("user_profiles" in sample_data):
            seed_user_profiles(sample_data["user_profiles"])
        if ("albums" in sample_data):
            seed_albums(sample_data["albums"])
        if ("songs" in sample_data):
            seed_songs(sample_data["songs"])
        sample_file.close()

def clear_data():
    Album.objects.all().delete()
    UserProfile.objects.filter(user__is_superuser=False).delete()
    User.objects.filter(is_superuser=False).delete()
    Song.objects.all().delete()
    Comment.objects.all().delete()

def seed_comments(comment_data,current_album):
    for comment in comment_data:
        #Skip if user is not found
        try:
            if "user__display_name" in comment:
                user_profile = UserProfile.objects.get(display_name=comment["user__display_name"])
            else:
                user_profile = UserProfile.objects.get(user__username=comment["user"])
            C = Comment(user=user_profile,text=comment["message"],album=current_album)
            C.save()
        except:
            pass

def seed_albums(album_data):
    for album in album_data:
        if album["cover"] == None: #"Default=" option does not seem to work if cover = null
            album.pop("cover")
        release_date = album.pop("release_date")
        release_date = datetime.strptime(release_date, "%Y-%m-%d").date()
        comments = album.pop("comments")
        A = Album(**album) #Use python dictionary unpack
        A.release_date = release_date
        A.save()
        seed_comments(comments,A)

def seed_user_profiles(user_profile_data):
    for user_profile in user_profile_data:
        user_data = user_profile["user"]
        user_email = None
        if "email" in user_data:
            user_email = user_data["email"]
        new_user = User.objects.create_user(username=user_data["username"], password=user_data["password"],email=user_email)
        UP = UserProfile(user=new_user,display_name=user_profile["display_name"])
        UP.save()

def seed_songs(song_data):
    for song in song_data:
        album_list = []
        for album_title in song["albums"]:
            song_albums = list(Album.objects.filter(title=album_title))
            album_list.extend(song_albums)
    
        S = Song(title=song["title"], runtime=song["runtime"])
        S.save()
        S.album.set(album_list)
        #Set outside creation because "Direct assignment to the forward side of a many-to-many set is prohibited"