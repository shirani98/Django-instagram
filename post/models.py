from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

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
    class Meta:
       ordering = ['-created']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.body)[:10]
        super().save(*args, **kwargs)