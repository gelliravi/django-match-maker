"""Tests for the models of the ``checkins`` app."""
from django.test import TestCase

from checkins.models import Checkin
from checkins.tests.factories import CheckinFactory


class CheckinTestCase(TestCase):
    """Tests for the ``Checkin`` model class."""
    def test_model(self):
        """Should be able to instantiate and save a Chekin object."""
        instance = CheckinFactory()
        self.assertTrue(instance.pk)

    def test_expires_prior_checkins(self):
        """Should expire prior checkins of this user when checking in again."""
        instance = CheckinFactory()
        instance2 = CheckinFactory(user=instance.user)
        instance = Checkin.objects.get(pk=instance.pk)
        self.assertTrue(instance.expired)
        self.assertFalse(instance2.expired)
