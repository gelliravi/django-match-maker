"""Tests for the ``expire_checkins`` admin command."""
from django.core.management import call_command
from django.test import TestCase
from django.utils.timezone import datetime, timedelta

from checkins.models import Checkin
from checkins.tests.factories import CheckinFactory


class ExpireCheckinsTestCase(TestCase):
    """Tests for the ``expire_checkins`` admin command."""
    def test_command(self):
        checkin = CheckinFactory()
        checkin.time = datetime.now() - timedelta(minutes=90)
        checkin.save()
        CheckinFactory()
        CheckinFactory()

        call_command('expire_checkins')
        self.assertEqual(Checkin.objects.filter(expired=True).count(), 1)
