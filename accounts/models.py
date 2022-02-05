from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            phone = phone,
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            phone = phone,
            username = username
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=13,unique=True,null=True, blank=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null= True)
    date_of_birth = models.DateField(blank=True, null= True)
    bio = models.TextField( blank=True)
    age = models.CharField(null=True, blank=True, max_length=2)
    phone = models.CharField(max_length=13,unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatar',default = '115-1150152_default-profile-picture-avatar-png-green.jpg')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone','username']
    
    objects = MyUserManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    
