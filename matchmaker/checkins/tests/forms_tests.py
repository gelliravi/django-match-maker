"""Tests for the forms of the ``checkins`` app."""
from django.test import TestCase

from django_libs.tests.factories import UserFactory

from checkins.forms import CheckinCreateForm, CheckoutForm
from checkins.models import Checkin
from checkins.tests.factories import CheckinFactory
from places.tests.factories import PlaceFactory, PlaceTypeFactory


class CheckinCreateFormTestCase(TestCase):
    """Tests for the ``CheckinCreateForm`` form class."""
    longMessage = True

    def setUp(self):
        super(CheckinCreateFormTestCase, self).setUp()
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
            'Errors: {0}'.format(form.errors.items())))
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


class CheckoutFormTestCase(TestCase):
    """Tests for the ``CheckoutForm`` form class."""
    longMessage = True

    def test_expires_all_checkins(self):
        checkin1 = CheckinFactory()
        checkin2 = CheckinFactory()
        form = CheckoutForm(user=checkin1.user, data={})
        self.assertTrue(form.is_valid(), msg=(
            'Errors: {0}'.format(form.errors.items())))
        form.save()
        checkin1 = Checkin.objects.get(pk=checkin1.pk)
        checkin2 = Checkin.objects.get(pk=checkin2.pk)
        self.assertTrue(checkin1.expired)
        self.assertFalse(checkin2.expired)
