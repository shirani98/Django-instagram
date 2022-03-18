from django.db import models
from django.shortcuts import get_object_or_404, redirect
from post.models import Post
from accounts.models import MyUser

# Create your models here.


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='postlike')
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='userlike')

    def __str__(self):
        return f"{self.user} liked {self.post.body [:5]} of {self.post.user}"

    def save(self, *args, **kwargs):
        liked = self.user.userlike.filter(post=self.post).exists()
        if liked:
            return False
        else:
            return super().save(*args, **kwargs)

    @classmethod
    def create_like(cls, postid, user):
        post_liked = get_object_or_404(Post, pk=postid)
        user_liked = get_object_or_404(MyUser, username=user)
        liked = Like(post=post_liked, user=user_liked)
        liked.save()
        return redirect('post:detail', post_liked.slug)

    @classmethod
    def delete_like(cls, postid, user):
        post_liked = get_object_or_404(Post, pk=postid)
        user_liked = get_object_or_404(MyUser, username=user)
        liked = Like.objects.get(post=post_liked, user=user_liked)
        liked.delete()
        return redirect('post:detail', post_liked.slug)
