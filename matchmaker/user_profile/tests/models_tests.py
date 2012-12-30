"""Tests for the models of the ``user_profile`` app."""
"""Tests for the models of the ``user_profile`` app."""
from django.test import TestCase
from django.utils import timezone

from django_libs.tests.factories import UserFactory
from user_profile.models import (
    UserProfile,
    create_profile_for_new_user,
    facebook_extra_values,
    new_users_handler,
    user_registered_handler,
)
from user_profile.tests.factories import UserProfileFactory


class CreateProfileForNewUserTestCase(TestCase):
    """Tests for the ``create_profile_for_new_user`` method."""
    def test_method(self):
        user = UserFactory()
        create_profile_for_new_user(user)
        self.assertEqual(UserProfile.objects.all().count(), 1, msg=(
            'When called with a new user it should create a new profile for'
            ' this user'))


class FacebookExtraValuesTestCase(TestCase):
    """Tests for the ``facebook_extra_values`` signal handler."""
    def test_handler(self):
        user = UserFactory()
        profile = UserProfileFactory(user=user)

        #empty response
        facebook_extra_values(self, user, {}, {})

        # This is how the response from facebook looks like. It contains many
        # more values but we only use these few.
        response = {
            'birthday': '09/08/1982',
            'gender': 'male',
            'username': 'Foo',
            'first_name': 'Foo',
            'last_name': 'Bar',
            'location': {
                'id': '101883206519751',
                'name': 'Singapore, Singapore', },
        }
        facebook_extra_values(self, user, response, {})

        profile = UserProfile.objects.get(pk=profile.pk)
        self.assertEqual(profile.birthday, timezone.datetime(
            1982, 9, 8).date(), msg=(
                'Should set the birthday correctly'))
        self.assertEqual(profile.gender, 'male', msg=(
            'Should set the gender correctly'))
        self.assertEqual(profile.location, 'Singapore, Singapore', msg=(
            'Should set the location correctly'))


class NewUsersHandlerTestCase(TestCase):
    """Tests for the ``new_users_handler`` signal handler."""
    def test_handler(self):
        user = UserFactory()
        new_users_handler(self, user, {}, {})
        self.assertEqual(UserProfile.objects.all().count(), 1, msg=(
            'When called with a new user it should create a new profile for'
            ' this user'))


class UserProfileTestCase(TestCase):
    """Tests for the ``UserProfile`` model."""
    def test_model(self):
        profile = UserProfileFactory()
        self.assertTrue(profile.pk)


class UserRegisteredHandlerTestCase(TestCase):
    """Tests for the ``user_registered_handler`` signal handler."""
    def test_should_save_user_profile(self):
        user = UserFactory.create()
        user_registered_handler(self, user, {})
        self.assertEqual(UserProfile.objects.all().count(), 1, msg=(
            'When called with a new user it should create a new profile for'
            ' this user'))
