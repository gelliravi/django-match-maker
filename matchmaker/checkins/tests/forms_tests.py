"""Tests for the forms of the ``checkins`` app."""
from django.test import TestCase

from django_libs.tests.factories import UserFactory

from checkins.forms import CheckinCreateForm
from places.tests.factories import PlaceFactory, PlaceTypeFactory


class CheckinCreateFormTestCase(TestCase):
    """Tests for the ``CheckinCreateForm`` form class."""
    longMessage = True

    def setUp(self):
        self.type = PlaceTypeFactory(name='Basketball')
        self.place = PlaceFactory()
        self.data = {
            'user_name': 'Martin',
            'lat': '1.3568494',
            'lng': '103.9478796',
        }

    def test_save_no_user(self):
        """Should create a checkin when username is given."""
        form = CheckinCreateForm(user=None, place=self.place, data=self.data)
        self.assertTrue(form.is_valid(), msg=(
            'Erorrs: {0}'.format(form.errors.items())))
        instance = form.save()
        self.assertTrue(instance.pk)

    def test_save_with_user(self):
        """Should create a checkin when user is given."""
        user = UserFactory()
        form = CheckinCreateForm(user=user, place=self.place, data=self.data)
        self.assertTrue(form.is_valid(), msg=(
            'Erorrs: {0}'.format(form.errors.items())))
        instance = form.save()
        self.assertTrue(instance.pk)
