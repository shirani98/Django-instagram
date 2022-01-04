from django.db import models
from django.contrib.auth.models import User
from post.models import Post
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='ucomment')
    post = models.ForeignKey(Post, on_delete= models.CASCADE,related_name='pcomment')
    is_reply = models.BooleanField(default=False)
    reply = models.ForeignKey('self', on_delete= models.CASCADE, null=True,blank=True, related_name='ccomment')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} = {self.body[:10]}"
    class Meta:
        ordering = ["-created"]
    