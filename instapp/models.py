import profile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='pics/',blank=True)
    img_name = models.CharField(max_length=200, blank=True)
    imge_caption = models.CharField(max_length=200,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True,blank=True)
    likes=models.IntegerField(default=0)

    def total_likes(self):
        return self.likess.count()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.img_name
 
class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=200, blank=True)
    profile_photo = models.ImageField(upload_to='pics/',blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True,blank=True)
    bio = models.TextField(max_length=200,blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name
 
class Comment(models.Model):
    post = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    poster = models.ForeignKey(User,on_delete=models.CASCADE,related_name='poster',null=True,blank=True)
    comment=models.TextField(null=True,blank=True)
    date_posted= models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment
 
class Likes(models.Model):
   user = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='user_likes')
   image = models.ForeignKey(Image,  on_delete=models.CASCADE, related_name='image_likes')











