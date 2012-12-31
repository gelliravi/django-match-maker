"""Tests for the ``pipeline.user`` functions."""
from django.contrib.auth.models import User
from django.test import TestCase

from django_libs.tests.factories import UserFactory

from matchmaker.pipeline.user import create_user, get_username


class CreateUserTestCase(TestCase):
    """Tests for the ``create_user`` function."""
    def test_create_user(self):
        user = UserFactory()
        resp = create_user(backend=None, details=None, response=None, uid=None,
                           username=None, user=user)
        self.assertEqual(resp, {'user': user}, msg=(
            'Should respond the user instance. Response was {0}'.format(resp)))
        resp = create_user(backend=None, details=None, response=None, uid=None,
                           username=None)
        self.assertIsNone(resp, msg=(
            'Should respond "None". Response was {0}'.format(resp)))
        resp = create_user(backend=None, details={'email': 'info@example.com'},
                           response=None, uid=None, username=user.username)
        self.assertEqual(resp, {'user': user, 'is_new': False}, msg=(
            'Should respond the user instance plus "not new"-notification.'
            'Response was {0}'.format(resp)))
        resp = create_user(backend=None, details={'email': 'info@example.com'},
                           response=None, uid=None, username='Foo')
        self.assertEqual(
            resp,
            {'user': User.objects.get(username='Foo'), 'is_new': True},
            msg=('Should respond the user instance plus "new"-notification.'
                 'Response was {0}'.format(resp)))

    """Tests for the ``get_username`` function."""
    def test_get_username(self):
        user = UserFactory()
        resp = get_username(details={'email': user.email}, user=user)
        self.assertEqual(resp, {'username': user.username}, msg=(
            'Should respond the username. Response was {0}'.format(resp)))
        resp = get_username(details={'email': user.email})
        self.assertEqual(resp, {'username': user.username}, msg=(
            'Should respond the username. Response was {0}'.format(resp)))
        resp = get_username(details={'email': 'info@example.com'})
        self.assertTrue(resp['username'], msg=(
            'Should return a generated username. Response was'
            ' {0}'.format(resp['username'])))
