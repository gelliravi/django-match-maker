"""Tests for the views of the ``checkins`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewTestMixin

from checkins.models import Checkin
from checkins.tests.factories import CheckinFactory
from places.tests.factories import PlaceFactory


class CheckinCreateViewTestCase(ViewTestMixin, TestCase):
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


class CheckoutViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``CheckoutView`` view class."""
    def setUp(self):
        self.checkin = CheckinFactory()

    def get_view_name(self):
        return 'checkins_checkout'

    def test_needs_authentication(self):
        """Should redirect to login if user is not authenticated."""
        self.should_redirect_to_login_when_anonymous()

    def test_callable(self):
        """Should be callable when authenticated."""
        self.should_be_callable_when_authenticated(self.checkin.user)

    def test_checks_out_user(self):
        """Should check-out user when called with POST."""
        self.login(self.checkin.user)
        self.client.post(self.get_url())
        checkins = Checkin.objects.filter(
            user=self.checkin.user, expired=False)
        self.assertEqual(checkins.count(), 0)
