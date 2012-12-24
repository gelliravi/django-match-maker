"""Tests for the views of the ``checkins`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewTestMixin

from places.tests.factories import PlaceFactory


class CheckinCreateView(ViewTestMixin, TestCase):
    """Tests for the ``CheckinCreateView`` view class."""
    def setUp(self):
        self.place = PlaceFactory()

    def get_view_name(self):
        return 'checkins_create'

    def get_view_kwargs(self):
        return {'place_pk': self.place.pk, }

    def test_raises_404(self):
        """Should raise 404 if place does not exist."""
        url = self.get_url(view_kwargs={'place_pk': 999, })
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_view(self):
        """CheckinCreateView is callable when logged in."""
        self.should_be_callable_when_anonymous()
