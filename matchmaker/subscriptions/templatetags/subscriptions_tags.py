"""Templatetags for the ``subscriptions`` app."""
from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.assignment_tag
def get_ctype(obj):
    return ContentType.objects.get_for_model(obj)
