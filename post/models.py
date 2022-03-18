from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from random import randint
from django.db.models import Q

from follow.models import Relation


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='userpost')
    image = models.ImageField(upload_to='post')
    body = models.TextField(max_length=255)
    slug = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.body}"

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if Post.objects.filter(slug=self.slug).exists():
            extra = str(randint(1, 10000000))
            self.slug = slugify(self.body)[:20] + "-" + extra
        else:
            self.slug = slugify(self.body)[:20]
        super().save(*args, **kwargs)

    @classmethod
    def show_feed(cls, user):
        if user.is_authenticated:
            followed_people = Relation.objects.filter(
                from_user=user).values('to_user')
            queryset = Post.objects.filter(
                Q(user__in=followed_people) | Q(user=user))
        else:
            queryset = Post.objects.all()
        return queryset
