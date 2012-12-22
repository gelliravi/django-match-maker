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
    )

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
