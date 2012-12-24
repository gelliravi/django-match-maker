"""Tests for the templatetags of the ``checkins`` app."""
from django.test import TestCase

from checkins.templatetags.checkins_tags import get_checkins
from checkins.tests.factories import CheckinFactory


class GetCheckinsTestCase(TestCase):
    """Tests for the ``get_checkins()`` templatetag."""
    longMessage = True

    def test_tag(self):
        """
        Should return the checkins for the place that are not yet expired.

        """
        # Two checkins that are valid
        checkin1_1 = CheckinFactory()
        CheckinFactory(place=checkin1_1.place)

        # One checkin that is expired
        checkin1_3 = CheckinFactory(place=checkin1_1.place)
        checkin1_3.expired = True
        checkin1_3.save()

        # One checkin that belongs to another place
        CheckinFactory()

        result = get_checkins(checkin1_1.place)
        self.assertEqual(result.count(), 2)
