from post.models import Post
from django.shortcuts import get_object_or_404, redirect
from accounts.models import MyUser
from like.models import Like
from django.views.generic.list import ListView
from django.views.generic import View


class LikePost(View):

    def get(self, request, *args, **kwargs):
        post_liked = get_object_or_404(Post, pk=kwargs['postid'])
        user_liked = get_object_or_404(MyUser, username=request.user.username)
        liked = Like(post=post_liked, user=user_liked)
        liked.save()
        return redirect('post:detail', post_liked.slug)


class UnLikePost(View):

    def get(self, request, *args, **kwargs):
        post_liked = get_object_or_404(Post, pk=kwargs['postid'])
        user_liked = get_object_or_404(MyUser, username=request.user.username)
        liked = Like.objects.get(post=post_liked, user=user_liked)
        liked.delete()
        return redirect('post:detail', post_liked.slug)


class LikeList(ListView):
    template_name = 'like/likelist.html'

    def get_queryset(self, *args, **kwargs):
        post = Post.objects.get(slug=self.kwargs['slug'])
        return post.postlike.all()
