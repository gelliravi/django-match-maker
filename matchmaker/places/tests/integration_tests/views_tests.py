"""Tests for the views of the ``places`` app."""
from django.test import TestCase, RequestFactory

from django_libs.tests.mixins import ViewTestMixin

from places.tests.factories import PlaceFactory
from places.views import PlaceListView


class PlaceCreateViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``CreatePlaceView`` view class."""
    def get_view_name(self):
        return 'places_create'

    def test_view(self):
        """Should be callable when anonymous."""
        self.should_be_callable_when_anonymous()


class PlaceDetailViewTestCase(ViewTestMixin, TestCase):
    """Test for the ``PlaceDetailView`` view class."""
    def setUp(self):
        super(PlaceDetailViewTestCase, self).setUp()
        self.place = PlaceFactory()

    def get_view_name(self):
        return 'places_detail'

    def get_view_kwargs(self):
        return {'pk': self.place.pk, }

    def test_view(self):
        """Should be callable when anonymous."""
        self.should_be_callable_when_anonymous()


class PlacesListViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``PlacesListView`` view class."""
    def get_view_name(self):
        return 'places_list'

    def test_view(self):
        """PlacesListView should be callable when anonymous."""
        self.should_be_callable_when_anonymous()

    # TODO enable this test when the problem with the test db has been solved
    def _test_post_no_places(self):
        """PlacesListView should return [] when no places exist."""
        req = RequestFactory().post(self.get_url(), data={'lat': 1, 'lng': 2})
        resp = PlaceListView().dispatch(req)
        self.assertEqual(resp.context_data['places'], [])

    # TODO enable this test when the problem with the test db has been solved
    def _test_post(self):
        """PlacesListView should return nearby places when point is given."""
        PlaceFactory()
        data = {'lat': 1.3568494, 'lng': 103.9478796}
        req = RequestFactory().post(self.get_url(), data=data)
        resp = PlaceListView().dispatch(req)
        self.assertEqual(len(resp.context_data['places']), 1)
