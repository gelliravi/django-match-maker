"""Models for the ``checkins`` app."""
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Checkin(models.Model):
    """
    An event, when a user checks in at a place.

    :user: The user who checked in.
    :place: The place where the user checked in.
    :point: The exact position of the user when he checked in.
    :time: Time when the user checked in.

    """
    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        null=True, blank=True,
    )

    user_name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
        blank=True,
    )

    place = models.ForeignKey(
        'places.Place',
        verbose_name=_('Place'),
    )

    point = models.PointField(
        geography=True,
        verbose_name=_('Point'),
    )

    time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Time'),
    )

    objects = models.GeoManager()

    def __unicode__(self):
        return '{0} @ {1}'.format(self.user.email, self.place.name)
