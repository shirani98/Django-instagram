from django.core.management import BaseCommand
from accounts.models import MyUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        MyUser.objects.update(is_active=True)
