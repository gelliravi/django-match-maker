"""Templatetags for the ``matchmaker`` project."""
from django import template

from checkins.models import Checkin


register = template.Library()


@register.assignment_tag
def get_checkins_for_place(user, place):
    return Checkin.objects.filter(user=user, place=place)
