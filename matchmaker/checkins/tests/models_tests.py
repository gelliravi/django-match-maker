"""Tests for the models of the ``checkins`` app."""
from django.test import TestCase

from checkins.tests.factories import CheckinFactory


class CheckinTestCase(TestCase):
    """Tests for the ``Checkin`` model class."""
    def test_model(self):
        """Should be able to instantiate and save a Chekin object."""
        instance = CheckinFactory()
        self.assertTrue(instance.pk)
