"""Tests for the forms of the ``subscriptions`` app."""
from django.test import TestCase

from django_libs.tests.factories import UserFactory

from subscriptions.forms import SubscriptionCreateForm
from subscriptions.tests.factories import DummyModelFactory


class SubscriptionCreateFormTestCase(TestCase):
    """Tests for the ``SubscriptionCreateForm`` form class."""
    longMessage = True

    def test_save(self):
        """Should create a new subscription."""
        user = UserFactory()
        dummy = DummyModelFactory()
        form = SubscriptionCreateForm(user=user, content_object=dummy, data={})
        self.assertTrue(form.is_valid(), msg=(
            'Errors: {0}'.format(form.errors.items())))
        instance = form.save()
        self.assertTrue(instance.pk)
