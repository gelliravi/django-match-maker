"""Tests for the views of the ``places`` app."""
from django.test import TestCase, RequestFactory

from django_libs.tests.mixins import ViewTestMixin

from places.views import PlaceListView


class CreatePlaceViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``CreatePlaceView`` view class."""
    def get_view_name(self):
        return 'places_create'

    def test_view(self):
        """CreatePlaceView should be callable when anonymous."""
        self.should_be_callable_when_anonymous()


class PlacesListViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``PlacesListView`` view class."""
    def get_view_name(self):
        return 'places_list'

    def test_view(self):
        """PlacesListView should be callable when anonymous."""
        self.should_be_callable_when_anonymous()

    def test_post(self):
        """PlacesListView should return nearby places when given a point."""
        req = RequestFactory().post(self.get_url(), data={'lat': 1, 'lng': 2})
        resp = PlaceListView().dispatch(req)
        self.assertTrue('places' in resp.context_data)
