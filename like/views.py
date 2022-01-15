from django.shortcuts import render
from post.models import Post
from django.shortcuts import get_object_or_404 , redirect
from accounts.models import MyUser
from .models import Like
from django.views.generic.list import ListView

# Create your views here.
def like_post(request, postid):
    post_liked = get_object_or_404(Post, pk=postid)
    user_liked = get_object_or_404(MyUser, username = request.user.username)
    liked = Like(post = post_liked, user = user_liked)
    liked.save()
    return redirect('post:detail',post_liked.slug)

def unlike(request, postid):
    post_liked = get_object_or_404(Post, pk=postid)
    user_liked = get_object_or_404(MyUser, username = request.user.username)
    liked = Like.objects.get(post = post_liked, user = user_liked)
    liked.delete()
    return redirect('post:detail',post_liked.slug)

class LikeList(ListView):
    def get_queryset(self, *args, **kwargs):
        post = Post.objects.get(slug = self.kwargs['slug'])
        return post.postlike.all()
    template_name = 'like/likelist.html'