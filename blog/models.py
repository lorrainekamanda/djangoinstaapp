from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    profile_image = models.ImageField(upload_to = 'images/',blank = True)
    bio = models.TextField(max_length =1060,null = True)


    def __str__(self):
        return self.bio

class Image(models.Model):

    upload_image = models.ImageField(upload_to = 'images/',blank = True)
    caption = models.CharField(max_length =160,null = True)
    comments = models.TextField(max_length =1160,null = True)
    likes = models.IntegerField(null = True)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return self.image

