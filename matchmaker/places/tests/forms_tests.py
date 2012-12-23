"""Tests for the forms of the ``places`` app."""
from django.test import TestCase

from places.forms import CreatePlaceForm


class CreatePlaceFormTestCase(TestCase):
    """Tests for the ``CreatePlaceForm`` form class."""
    def test_adds_lat_lng_fields(self):
        """When initiated, the form should add hidden fields for lat/lng."""
        form = CreatePlaceForm()
        self.assertTrue('lat' in form.fields)
        self.assertTrue('lng' in form.fields)

    def test_save(self):
        """When saved, the form should create a ``Place`` object."""
        data = {
            'name': 'Test',
            'lat': 0,
            'lng': 0,
        }
        form = CreatePlaceForm(data=data)
        self.assertTrue(form.is_valid())
        instance = form.save()
        self.assertTrue(instance.pk)
