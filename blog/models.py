from django.db import models
from django.contrib.auth.models import User

# Create your models here.


        
class Profile(models.Model):

    profile_image = models.ImageField(default = 'profile.jpg',upload_to = 'images/')
    bio = models.TextField(max_length =160,null = True)
    phone_number = models.IntegerField(null = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE,null = True)

    @classmethod
    def search_by_username(cls,search_term):
        uses = cls.objects.filter(user__username__icontains=search_term)
        return uses

    def __str__(self):
        return self.user.username

class Image(models.Model):

    upload_image = models.ImageField(upload_to = 'images/',blank = True)
    caption = models.CharField(max_length =160,null = True)
    comments = models.TextField(max_length =1160,null = True)
    likes = models.IntegerField(null = True)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null = True)
    username= models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    
    
    def save_images(self):
        self.save()
   
    def delete_images(self):
        self.delete()

  
    def __str__(self):
        return self.image

