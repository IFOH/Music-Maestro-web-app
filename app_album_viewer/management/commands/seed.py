from django.core.management.base import BaseCommand
from app_album_viewer.models import *
from datetime import datetime
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        sample_file = open("sample_data/sample_data_copy.json")
        sample_data = json.load(sample_file)
        self.stdout.write('seeding data')
        if ("albums" in sample_data):
            seed_albums(sample_data["albums"])
        if ("user_profiles" in sample_data):
            seed_user_profiles(sample_data["user_profiles"])
        if ("songs" in sample_data):
            seed_songs(sample_data["songs"])
        if ("comments" in sample_data):
            seed_comments(sample_data["comments"])
        sample_file.close()
        self.stdout.write('done')

#Delete all data
def clear_data():
    Album.objects.all().delete()
    UserProfile.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()
    Song.objects.all().delete()
    Comment.objects.all().delete()

def seed_albums(album_data):
    for album in album_data:
        release_date = album.pop("release_date")
        release_date = datetime.strptime(release_date, "%Y-%m-%d").date()
        A = Album(**album) #Use python dictionary unpack
        A.release_date = release_date
        A.save()

def seed_user_profiles(user_profile_data):
    for user_profile in user_profile_data:
        user_data = user_profile["user"]
        new_user = User.objects.create_user(username=user_data.username, password=user_data.password)
        UP = UserProfile(user=new_user,display_name=user_profile["display_name"],email=user_profile["email"])
        UP.save()

def seed_comments(comment_data):
    pass

def seed_songs(song_data):
    for song in song_data:
        album_list = []
        for album_title in song["albums"]:
            song_albums = list(Album.objects.filter(title=album_title))
            album_list.extend(song_albums)
    
        S = Song(title=song["title"], runtime=song["runtime"])
        S.save()
        S.album.set(album_list) #Prevents typerror: Direct assignment to the forward side of a many-to-many set is prohibited