"""Context processors for the ``matchmaker`` project."""
from django.conf import settings


def analytics(request):
    return {
        'ANALYTICS_TRACKING_ID': getattr(
            settings, 'ANALYTICS_TRACKING_ID', 'UA-XXXXXXX-XX'),
    }
