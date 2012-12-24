"""Command that expires old checkins."""
from django.core.management.base import BaseCommand
from django.utils.timezone import datetime, timedelta

from checkins.models import Checkin


class Command(BaseCommand):
    help = 'Expires checkins older than X minutes.'

    def handle(self, *args, **options):
        Checkin.objects.filter(
            time__lte=datetime.now() - timedelta(minutes=90)).update(
                expired=True)
        self.stdout.write('Successfully expired old checkins.')
