"""Tests for the forms of the ``places`` app."""
from django.test import TestCase

from places.forms import PlaceCreateForm
from places.tests.factories import PlaceTypeFactory


class PlaceCreateFormTestCase(TestCase):
    """Tests for the ``PlaceCreateForm`` form class."""
    def setUp(self):
        super(PlaceCreateFormTestCase, self).setUp()
        self.type = PlaceTypeFactory(name='Basketball')

    def test_adds_lat_lng_fields(self):
        """
        When initiated, PlaceCreateForm should add hidden fields for lat/lng.

        """
        form = PlaceCreateForm()
        self.assertTrue('lat' in form.fields)
        self.assertTrue('lng' in form.fields)

    def test_save(self):
        """When saved, PlaceCreateForm should create a ``Place`` object."""
        data = {
            'name': 'Test',
            'lat': 0,
            'lng': 0,
        }
        form = PlaceCreateForm(data=data)
        self.assertTrue(form.is_valid())
        instance = form.save()
        self.assertTrue(instance.pk)
