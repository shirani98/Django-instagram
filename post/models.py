from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    body = models.TextField()
    slug = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} {self.body}"
    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'year': self.created.year,'month': self.created.month,'day': self.created.day,'slug': self.slug})
    