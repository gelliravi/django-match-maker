"""Tests for the templatetags of the ``checkins`` app."""
from django.test import TestCase
from django.contrib.auth.models import AnonymousUser

from django_libs.tests.factories import UserFactory

from checkins.templatetags.checkins_tags import (
    get_checkins,
    get_checked_in_place,
)
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


class GetCheckedInPlace(TestCase):
    """Tests for the ``get_checked_in_place`` templatetag."""
    longMessage = True

    def test_tag_with_user(self):
        """Should return the place where the given user is checked-in."""
        checkin = CheckinFactory()
        result = get_checked_in_place(checkin.user)
        self.assertEqual(result, checkin.place)

    def test_tag_without_checkin(self):
        """Should return `None` if the user is not checked-in anywhere."""
        user = UserFactory()
        result = get_checked_in_place(user)
        self.assertEqual(result, None)

    def test_tag_without_user(self):
        """Should return `None` if the user is anonymous."""
        user = AnonymousUser()
        result = get_checked_in_place(user)
        self.assertEqual(result, None)
