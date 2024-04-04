from django.db import models
from authentication.models import *

# Create your models here.
class Club(models.Model):
    profilePhoto = models.ImageField(upload_to='profile_photos/Clubs')
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=5000)
    admins = models.ManyToManyField(User)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='events/')
    description = models.TextField(max_length=5000)
    dateTime = models.DateTimeField()
    venue = models.TextField(max_length=500)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)