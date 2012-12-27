"""Tests for the views of the ``user_profile`` app."""
from django.test import TestCase

from django_libs.tests.factories import UserFactory
from django_libs.tests.mixins import ViewTestMixin


class UserProfileUpdateViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``UserProfileUpdateView`` view class."""
    def get_view_name(self):
        return 'user_profile_update'

    def setUp(self):
        super(UserProfileUpdateViewTestCase, self).setUp()
        self.user = UserFactory()

    def test_login_reqired(self):
        self.should_redirect_to_login_when_anonymous()
