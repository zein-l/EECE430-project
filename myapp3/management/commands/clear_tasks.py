from django.core.management.base import BaseCommand
from myapp3.models import Task  # Replace 'myapp3' with the name of your app

class Command(BaseCommand):
    help = 'Deletes all tasks'

    def handle(self, *args, **kwargs):
        Task.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all tasks'))
