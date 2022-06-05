import profile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='pics/',blank=True)
    img_name = models.CharField(max_length=200, blank=True)
    imge_caption = models.CharField(max_length=200,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True,blank=True)
    # comment = models.ForeignKey(Comment, blank=True,null=True)

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
    comment = models.TextField(max_length=200,null=True, blank=True)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment
 
class Likes(models.Model):
   user = models.ForeignKey(Profile,  on_delete=models.CASCADE)
   image = models.ForeignKey(Image,  on_delete=models.CASCADE)











