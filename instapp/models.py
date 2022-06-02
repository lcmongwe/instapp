import profile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Models):
    Photo=models.ImageField()
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    bio= models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Comment(models.Model):
    comment= models.TextField()
    author=models.ForeignKey(Profile, null=True)


    def __str__(self):
            return self.comment

class Image(models.Model):
    name = models.CharField('Venue Name',max_length=120)
    image=models.ImageField()
    captions = models.CharField(max_length=200)
    profile= models.ForeignKey(Profile)
    likes= models.IntegerField(default=0)
    comments= models.TextChoices  

    def __str__(self):
        return self.name