from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255, blank=True, null=True)
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        if self.display_name == None:
            return self.user.username
        else:
            return self.display_name

class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length = 255)
    runtime = models.IntegerField(default=0)
    album = models.ManyToManyField(Album, blank=True)
    def __str__(self):
        return self.title