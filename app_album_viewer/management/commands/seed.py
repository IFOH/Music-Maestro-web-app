from django.core.management.base import BaseCommand
from app_album_viewer.models import *
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        sample_file = open("sample_data/sample_data_copy.json")
        sample_data = json.load(sample_file)
        self.stdout.write('seeding data')
        if ("albums" in sample_data):
            seed_albums(sample_data["albums"])
        if ("users" in sample_data):
            seed_users(sample_data["users"])
        if ("songs" in sample_data):
            seed_songs(sample_data["songs"])
        sample_file.close()
        self.stdout.write('done')

#Delete all data
def clear_data():
    pass

def seed_albums(album_data):
    for album in album_data:
        a = Album(title=album["title"])
        a.save()

def seed_users(user_data):
    pass

def seed_songs(song_data):
    for song in song_data:
        album_list = []
        for album_title in song["albums"]:
            album_list.append(Album.objects.get(title=album_title))
    
        s = Song(title=song["title"],runtime=song["runtime"],album=album_list)
        s.save()