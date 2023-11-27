from django.db import models

class Album(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100, blank=True, null=True)
    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ManyToManyField(Album, blank=True, null=True)

    def __str__(self):
        return self.title