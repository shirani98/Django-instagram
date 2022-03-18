from django.views.generic.list import ListView
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import MyUser
from follow.models import Relation


class FollowUser(View):

    def get(self, request, *args, **kwargs):
        return Relation.create_follow(kwargs['id'], request.user)


class UnFollowUser(View):

    def get(self, request, *args, **kwargs):
        return Relation.create_unfollow(kwargs['id'], request.user)


class FollowerList(ListView):
    template_name = 'follow/followlist.html'

    def get_queryset(self, *args, **kwargs):
        return Relation.objects.filter(to_user__username=self.kwargs['user'])


class FollowingList(ListView):
    template_name = 'follow/followinglist.html'

    def get_queryset(self, *args, **kwargs):
        return Relation.objects.filter(from_user__username=self.kwargs['user'])
