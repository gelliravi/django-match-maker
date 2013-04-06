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
        related_name='checkins',
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
        related_name='checkins',
    )

    point = models.PointField(
        geography=True,
        verbose_name=_('Point'),
    )

    time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Time'),
    )

    expired = models.BooleanField(
        default=False,
        verbose_name=_('Expired'),
    )

    objects = models.GeoManager()

    def __unicode__(self):
        if self.user:
            username = self.user.email
        else:
            username = self.user_name
        return '{0} @ {1}'.format(username, self.place.name)

    def save(self, *args, **kwargs):
        if self.user:
            Checkin.objects.filter(user=self.user, expired=False).update(
                expired=True)
        super(Checkin, self).save(*args, **kwargs)
