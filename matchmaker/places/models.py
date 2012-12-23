"""Models of the ``places`` app."""
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Place(models.Model):
    """
    Any place on earth.

    :name: The name of the place.
    :point: Lat/Lng of the place.
    :type: Optional type of the place.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    point = models.PointField(
        verbose_name=_('Point'),
        geography=True,
    )

    type = models.ForeignKey(
        'places.PlaceType',
        verbose_name=_('Type'),
        null=True, blank=True,
    )

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name


class PlaceType(models.Model):
    """
    A masterdata table holding types of places.

    :name: The name of the type.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    def __unicode__(self):
        return self.name
