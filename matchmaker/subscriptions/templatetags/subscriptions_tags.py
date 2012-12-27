"""Templatetags for the ``subscriptions`` app."""
from django import template
from django.contrib.contenttypes.models import ContentType

from subscriptions.models import Subscription


register = template.Library()


@register.assignment_tag
def get_ctype(obj):
    """
    Returns the ``ContentType`` for the given object.

    :param obj: Any object.

    """
    return ContentType.objects.get_for_model(obj)


@register.assignment_tag
def is_subscribed(user, obj):
    """
    Returns ``True`` if the user is subscribed to the given object.

    :param user: A ``User`` instance.
    :param obj: Any object.

    """
    ctype = ContentType.objects.get_for_model(obj)

    try:
        Subscription.objects.get(
            user=user, content_type=ctype, object_id=obj.pk)
    except Subscription.DoesNotExist:
        return False

    return True
