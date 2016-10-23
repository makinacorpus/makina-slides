from django.utils import timezone
from datetime import timedelta
from django.core.management.base import BaseCommand

from todo.models import Task


class Command(BaseCommand):
    args = '...'
    help = 'Do specific administration stuff'

    def handle(self, *args, **options):
        now = timezone.now()
        one_week_ago = now - timedelta(days=7)
        Task.objects.filter(
            deadline__lte=one_week_ago, done=True
        ).delete()
