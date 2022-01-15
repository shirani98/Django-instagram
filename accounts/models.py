from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    age = models.CharField(null=True, blank=True, max_length=2)
    phone = models.CharField(max_length=13,unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatar',default = '115-1150152_default-profile-picture-avatar-png-green.jpg')
    
    
