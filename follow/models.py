from django.db import models
from django.shortcuts import get_object_or_404, redirect
from accounts.models import MyUser

# Create your models here.


class Relation(models.Model):
    from_user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='fromuser')
    to_user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='touser')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} to {self.to_user}"

    class Meta:
        ordering = ['-created']

    @classmethod
    def create_follow(cls, user_for_follow, user):
        user_for_follow = get_object_or_404(MyUser, pk=user_for_follow)
        if Relation.objects.filter(
                from_user=user, to_user=user).exists():
            return redirect("accounts:profile", user=user_for_follow)
        Relation(from_user=user, to_user=user_for_follow).save()
        return redirect("accounts:profile", user=user_for_follow)

    @classmethod
    def create_unfollow(cls, user_for_unfollow, user):
        user_for_unfollow = get_object_or_404(MyUser, pk=user_for_unfollow)
        if Relation.objects.filter(
                from_user=user, to_user=user_for_unfollow).exists():
            get = get_object_or_404(
                Relation, from_user=user, to_user=user_for_unfollow)
            get.delete()
            return redirect("accounts:profile", user=user_for_unfollow)
        return redirect("accounts:profile", user=user_for_unfollow)
