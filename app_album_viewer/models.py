from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Album(models.Model):
    cover = models.ImageField(default="default-cover.png")
    title = models.CharField(max_length=255, default="Album title")
    description = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=255, default="Artist")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    format = models.CharField(max_length=2, choices=[("DD","Digital download"),("CD","CD"),("VN","Vinyl")], default="DD")
    release_date = models.DateField(default=timezone.now().date())

    def save(self, *args, **kwargs):
        if (self.release_date > timezone.now().date() + timezone.timedelta(days=365)):
            self.release_date = timezone.now().replace(year=self.release_date.year, month=1, day=1).date()
        super().save(*args, **kwargs)
        
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
    title = models.CharField(max_length=255)
    runtime = models.IntegerField(default=0)
    album = models.ManyToManyField(Album, blank=True)
    def __str__(self):
        return self.title