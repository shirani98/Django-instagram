from django.views.generic.list import ListView
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import MyUser
from .models import Relation


class FollowUser(View):
    
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(MyUser, pk = kwargs['id'] )
        check_status = Relation.objects.filter(from_user= request.user, to_user=user).exists()
        if check_status:
            return redirect("accounts:profile", user = user )
        else:
            Relation(from_user = request.user , to_user = user).save()
            return redirect("accounts:profile", user = user )


class UnFollowUser(View):
    
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(MyUser, pk =kwargs['id'])
        check_status = Relation.objects.filter(from_user= request.user, to_user=user).exists()
        if check_status:
            get = get_object_or_404(Relation , from_user = request.user , to_user = user)
            get.delete()
            return redirect("accounts:profile", user = user )
        else:
            return redirect("accounts:profile", user = user )


class FollowerList(ListView):
    template_name = 'follow/followlist.html'

    def get_queryset(self, *args, **kwargs):
        account = self.kwargs['user']
        user = MyUser.objects.get(username= account)
        return Relation.objects.filter(to_user = user)
    
class FollowingList(ListView):
    template_name = 'follow/followinglist.html'

    def get_queryset(self, *args, **kwargs):
        account = self.kwargs['user']
        user = MyUser.objects.get(username= account)
        return Relation.objects.filter(from_user = user)
