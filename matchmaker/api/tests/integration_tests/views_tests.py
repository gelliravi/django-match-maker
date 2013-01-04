"""Tests for the views of the ``api`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewTestMixin

from user_profile.tests.factories import UserProfileFactory


class UserCountAPIViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``UserCountAPIView`` view class."""
    def get_view_name(self):
        return 'api_user_count'

    def test_view(self):
        UserProfileFactory()
        UserProfileFactory()
        resp = self.client.get(self.get_url())
        self.assertEqual(resp.content, '"2"')
