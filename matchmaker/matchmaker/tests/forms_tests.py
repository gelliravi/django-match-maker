"""Tests for the forms of the ``matchmaker`` project."""
from django.test import TestCase

from matchmaker.forms import CustomCheckinCreateForm
from places.tests.factories import PlaceFactory
from user_profile.models import UserProfile
from user_profile.tests.factories import UserProfileFactory


class CustomCheckinCreateFormTestCase(TestCase):
    """Tests for the ``CustomCheckinCreateForm`` form class."""
    def setUp(self):
        super(CustomCheckinCreateFormTestCase, self).setUp()
        self.profile = UserProfileFactory()
        self.place = PlaceFactory()
        self.data = {
            'user_name': 'Foobar',
            'lat': '1.3568494',
            'lng': '103.9478796',
        }

    def test_adds_user_name_field(self):
        """Should add the user_name field if the user has no display name."""
        form = CustomCheckinCreateForm(
            user=self.profile.user, place=self.place, data={})
        self.assertTrue('user_name' in form.fields)

    def test_does_not_add_user_name_field(self):
        """Shouldn't add user_name field if the user has a display name."""
        self.profile.display_name = 'Foobar'
        self.profile.save()
        form = CustomCheckinCreateForm(
            user=self.profile.user, place=self.place, data={})
        self.assertFalse('user_name' in form.fields)

    def test_save(self):
        """
        Should set the user's display name when saved.

        That way the user only has to set it once on the first check-in.

        """
        self.assertEqual(self.profile.display_name, '')
        form = CustomCheckinCreateForm(
            user=self.profile.user, place=self.place, data=self.data)
        self.assertTrue(form.is_valid(), msg=(
            'Errors: {0}'.format(form.errors.items())))
        form.save()
        profile = UserProfile.objects.get(pk=self.profile.pk)
        self.assertEqual(profile.display_name, 'Foobar')
