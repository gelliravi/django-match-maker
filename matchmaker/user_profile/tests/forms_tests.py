"""Tests for the forms of the ``user_profile`` app."""
from django.test import TestCase

from user_profile.forms import UserProfileUpdateForm


class UserProfileUpdateFormTestCase(TestCase):
    """Tests for the ``UserProfileUpdateForm`` form class."""
    longMessage = True

    def setUp(self):
        super(UserProfileUpdateFormTestCase, self).setUp()
        self.data = {'timezone': 'Asia/Singapore', }

    def test_form(self):
        form = UserProfileUpdateForm(data=self.data)
        self.assertTrue(form.is_valid(), msg=(
            'Errors: {0}'.format(form.errors.items())))
