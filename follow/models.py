from django.db import models
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
