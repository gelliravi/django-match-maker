"""Models of the ``places`` app."""
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Place(models.Model):
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
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    def __unicode__(self):
        return self.name
