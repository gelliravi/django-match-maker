"""Factories for the ``user_profile`` app."""
import factory

from django_libs.tests.factories import UserFactory

from user_profile.models import UserProfile


class UserProfileFactory(factory.Factory):
    """Factory for the ``UserProfile`` model."""
    FACTORY_FOR = UserProfile

    user = factory.SubFactory(UserFactory)
