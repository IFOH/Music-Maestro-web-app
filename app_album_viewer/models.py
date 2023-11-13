from django.db import models

class Album(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100, blank = True)
    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.title