from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from random import randint
from accounts.models import MyUser

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'post')
    body = models.TextField(max_length=255)
    slug = models.CharField(max_length=50,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} {self.body}"
    
    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})
    
    class Meta:
       ordering = ['-created']
    
    def save(self, *args, **kwargs):
        if Post.objects.filter(slug=self.slug).exists():
            extra = str(randint(1, 10000000))
            self.slug = slugify(self.body)[:20] + "-" + extra
        else:
            self.slug = slugify(self.body)[:20]
        super().save(*args, **kwargs)
        
