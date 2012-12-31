"""Tests for the views of the ``user_profile`` app."""
from django.test import TestCase
from django.core.urlresolvers import reverse

from django_libs.tests.factories import UserFactory
from django_libs.tests.mixins import ViewTestMixin

from user_profile.models import UserProfile
from user_profile.tests.factories import UserProfileFactory


class UserProfileUpdateViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``UserProfileUpdateView`` view class."""
    def setUp(self):
        super(UserProfileUpdateViewTestCase, self).setUp()
        self.profile = UserProfileFactory()
        self.post_data = {
            'timezone': 'Asia/Singapore',
        }

    def get_view_name(self):
        return 'user_profile_update'

    def test_login_reqired(self):
        """Should redirect to login if anonymous."""
        self.should_redirect_to_login_when_anonymous()

    def test_callable(self):
        """Should be callable if user is authenticated."""
        self.should_be_callable_when_authenticated(self.profile.user)

    def test_creates_profile(self):
        """Should create a profile if a user doesn't have one."""
        user_without_profile = UserFactory()
        self.login(user_without_profile)
        self.client.get(self.get_url())
        profile = user_without_profile.get_profile()
        self.assertTrue(profile.pk)

    def test_save(self):
        """Should save the profile on POST request."""
        self.login(self.profile.user)
        self.client.post(self.get_url(), data=self.post_data)
        profile = UserProfile.objects.get(pk=self.profile.pk)
        self.assertEqual(profile.timezone, 'Asia/Singapore')


class UsernameUpdateViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``UniqueNameUpdateView`` view class."""
    longMessage = True

    def setUp(self):
        super(UsernameUpdateViewTestCase, self).setUp()
        self.profile = UserProfileFactory()

    def get_view_name(self):
        return 'user_profile_username_update'

    def test_login_required(self):
        """Should redirect to login if anonymous."""
        self.should_redirect_to_login_when_anonymous()

    def test_callable(self):
        """Should be callable if user is authenticated."""
        self.should_be_callable_when_authenticated(self.profile.user)

    def test_not_callable(self):
        """
        Should redirect to profile if user has already taken his username.

        """
        self.profile.username = 'foobar'
        self.profile.save()
        self.login(self.profile.user)
        resp = self.client.get(self.get_url())
        self.assertRedirects(resp, reverse('user_profile_update'))

    def test_save(self):
        """Should save the username on a POST request."""
        self.login(self.profile.user)
        self.client.post(self.get_url(), data={'username': 'foobar'})
        profile = UserProfile.objects.get(pk=self.profile.pk)
        self.assertEqual(profile.username, 'foobar')
