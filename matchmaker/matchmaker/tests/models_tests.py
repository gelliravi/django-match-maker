"""Tests for the signal handlers of the ``matchmaker`` project."""
from django.test import TestCase

from mailer.models import Message

from checkins.tests.factories import CheckinFactory
from places.tests.factories import PlaceFactory
from subscriptions.tests.factories import SubscriptionFactory


class SendCheckinNotificationsTestCase(TestCase):
    """Tests for the ``send_checkin_notifications`` signal handler."""
    longMessage = True

    def test_handler(self):
        place = PlaceFactory()

        # Two users are subscribed to the same place
        SubscriptionFactory(content_object=place)
        SubscriptionFactory(content_object=place)

        # A third user is subscribed to something else
        SubscriptionFactory()

        CheckinFactory(place=place)
        message = Message.objects.all()[0]
        self.assertEqual(len(message.to_addresses), 2)
