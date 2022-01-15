from django.db import models
from post.models import Post
from accounts.models import MyUser

# Create your models here.
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name = 'postlike')
    user = models.ForeignKey(MyUser, on_delete= models.CASCADE, related_name = 'userlike')
    def __str__(self):
        return f"{self.user} liked {self.post.body [:5]} of {self.post.user}"
    
    def save(self, *args, **kwargs):
        liked = self.user.userlike.filter(post=self.post).exists()
        if liked:
            return False
        else:
            return super().save(*args, **kwargs)