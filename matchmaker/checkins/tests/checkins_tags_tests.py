"""Tests for the templatetags of the ``checkins`` app."""
from django.test import TestCase

from checkins.templatetags.checkins_tags import get_checkins
from checkins.tests.factories import CheckinFactory


class GetCheckinsTestCase(TestCase):
    """Tests for the ``get_checkins()`` templatetag."""
    def test_tag(self):
        checkin1_1 = CheckinFactory()
        checkin1_2 = CheckinFactory(place=checkin1_1.place)
        checkin2 = CheckinFactory()
        result = get_checkins(checkin1_1.place)
        self.assertEqual(result.count(), 2)
