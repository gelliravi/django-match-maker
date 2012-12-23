"""Tests for the views of the ``places`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewTestMixin


class CreatePlaceViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``CreatePlaceView`` view class."""
    def get_view_name(self):
        return 'places_create'

    def test_view(self):
        """CreatePlaceView should be callable when anonymous."""
        self.should_be_callable_when_anonymous()
