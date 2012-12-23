"""Factories for the ``places`` app."""
from django.contrib.gis.geos import Point

import factory

from places.models import Place, PlaceType


class PlaceFactory(factory.Factory):
    FACTORY_FOR = Place

    name = 'Test Place'
    point = Point(1, 2)


class PlaceTypeFactory(factory.Factory):
    FACTORY_FOR = PlaceType

    name = 'Test Place Type'
