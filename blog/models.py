from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
# Create your models here.


        
class Profile(models.Model):

    profile_image = models.ImageField(default = 'profile.jpg',upload_to = 'images/')
    bio = models.TextField(max_length =160,null = True)
    phone_number = models.IntegerField(null = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE,blank = True,null = True)

   

    def __str__(self):
        return self.user.username

class Image(models.Model):

    image = models.ImageField(upload_to = 'images/',blank = True)
    caption = models.CharField(max_length =160,null = True,blank = True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null = True,blank = True)
    username= models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def get_comments(cls,image_id):

       image = Image.objects.get(pk = image_id)
       image_comments = image.comments.set_all()
       return image_comments


    def get_absolute_url(self):
        return reverse ('image-detail', kwargs = {'pk':self.pk})
   

    @classmethod
    def search_by_username(cls,search_term):
        uses = cls.objects.filter(username__user__icontains=search_term)
        return uses

    def get_image_by_id(id):
        image = Image.objects.get(id = image_id)
        return image
    
    def save_images(self):
        self.save()
   
    def delete_images(self):
        self.delete()

  
    def __str__(self):
        return self.username.username

class Comments(models.Model):
    comments = models.TextField(max_length =1160)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null = True,blank = True)
    likes = models.IntegerField(null = True,blank = True)
    username= models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse ('blog-home')

    def __str__(self):
        return self.username.username