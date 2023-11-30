from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100, blank=True, null=True)
    comment = models.JSONField
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ManyToManyField(Album, blank=True, null=True)
    def __str__(self):
        return self.title