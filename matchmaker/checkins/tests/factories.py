"""Factories for the ``checkins`` app."""
from django.contrib.gis.geos import Point

import factory
from django_libs.tests.factories import UserFactory

from checkins.models import Checkin
from places.tests.factories import PlaceFactory


class CheckinFactory(factory.Factory):
    FACTORY_FOR = Checkin

    user = factory.SubFactory(UserFactory)
    place = factory.SubFactory(PlaceFactory)
    point = Point(1, 2)
