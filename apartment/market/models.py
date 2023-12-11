from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fname = models.TextField('Name',max_length=50)
    lname = models.TextField('Name',max_length=60)
    email = models.EmailField(("Email"), max_length=254)
    image =models.ImageField(default='profiles/default.jpg',upload_to='profiles')
    
    def __str__(self):
        return f'{self.user.username} Profile'