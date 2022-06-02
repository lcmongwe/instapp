import profile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Models):
    Photo
    name
    bio


class Image(models.Model):
    name = models.CharField('Venue Name',max_length=120)
    image=models.ImageField()
    captions = models.CharField(max_length=200)
    profile= models.ForeignKey(Profile)
    likes= models.IntegerField(default=0)
    comments= models.TextChoices  

    def __str__(self):
        return self.name