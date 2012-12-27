"""Tests for the templatetags of the ``subscriptions`` app."""
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from subscriptions.templatetags.subscriptions_tags import get_ctype
from subscriptions.tests.factories import DummyModelFactory


class GetCtypeTestCase(TestCase):
    """Tests for the ``get_ctype`` templatetag."""
    def test_tag(self):
        dummy = DummyModelFactory()
        ctype = ContentType.objects.get_for_model(dummy)
        result = get_ctype(dummy)
        self.assertEqual(result, ctype)
