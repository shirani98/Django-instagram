from post.models import Post
from django.shortcuts import get_object_or_404, redirect
from accounts.models import MyUser
from like.models import Like
from django.views.generic.list import ListView
from django.views.generic import View


class LikePost(View):

    def get(self, request, *args, **kwargs):
        return Like.create_like(kwargs['postid'], self.request.user.username)


class UnLikePost(View):

    def get(self, request, *args, **kwargs):
        return Like.delete_like(kwargs['postid'], self.request.user.username)


class LikeList(ListView):
    template_name = 'like/likelist.html'

    def get_queryset(self, *args, **kwargs):
        post = Post.objects.get(slug=self.kwargs['slug'])
        return post.postlike.all()
