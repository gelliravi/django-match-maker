"""Templatetags for the ``checkins`` app."""
from django import template

register = template.Library()

from checkins.models import Checkin


@register.assignment_tag
def get_checkins(place):
    checkins = Checkin.objects.filter(place=place, expired=False)
    return checkins
