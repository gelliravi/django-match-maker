"""Templatetags for the ``checkins`` app."""
from django import template

register = template.Library()

from checkins.models import Checkin


@register.assignment_tag
def get_checkins(place):
    """
    Returns all checkins for a given place.

    :param place: A ``Place`` instance.

    """
    checkins = Checkin.objects.filter(place=place, expired=False)
    return checkins


@register.assignment_tag
def get_checked_in_place(user):
    """
    Returns the place where the given user is checked-in or ``None``.

    :param user: A ``User`` instance.

    """
    if not user.is_authenticated():
        return None
    try:
        checkin = Checkin.objects.get(user=user, expired=False)
    except Checkin.DoesNotExist:
        return None
    return checkin.place
