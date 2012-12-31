"""Tests for the forms of the ``user_profile`` app."""
from django.test import TestCase

from user_profile.forms import UsernameUpdateForm, UserProfileUpdateForm
from user_profile.tests.factories import UserProfileFactory


class UsernameUpdateFormTestCase(TestCase):
    """Tests for the ``UsernameUpdateForm`` form class."""
    longMessage = True

    def setUp(self):
        super(UsernameUpdateFormTestCase, self).setUp()
        self.data = {'username': 'foobar', }
        self.profile = UserProfileFactory()

    def test_form(self):
        """Should save the username."""
        form = UsernameUpdateForm(instance=self.profile, data=self.data)
        self.assertTrue(form.is_valid(), msg=(
            'Errors: {0}'.format(form.errors.items())))
        instance = form.save()
        self.assertEqual(instance.username, 'foobar')

    def test_unique(self):
        """Checks if username exists before saving."""
        self.profile.username = 'foobar'
        self.profile.save()
        form = UsernameUpdateForm(instance=self.profile, data=self.data)
        self.assertFalse(form.is_valid())
        self.assertTrue('username' in form.errors)


class UserProfileUpdateFormTestCase(TestCase):
    """Tests for the ``UserProfileUpdateForm`` form class."""
    longMessage = True

    def setUp(self):
        super(UserProfileUpdateFormTestCase, self).setUp()
        self.data = {'timezone': 'Asia/Singapore', }
        self.profile = UserProfileFactory()

    def test_form(self):
        """Should save the profile on valid data."""
        form = UserProfileUpdateForm(instance=self.profile, data=self.data)
        self.assertTrue(form.is_valid(), msg=(
            'Errors: {0}'.format(form.errors.items())))
        instance = form.save()
        self.assertEqual(instance.timezone, 'Asia/Singapore')
