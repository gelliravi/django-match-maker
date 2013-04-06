"""Context processors for the ``matchmaker`` project."""
from django.conf import settings


def context_settings(request):
    return {
        'ANALYTICS_TRACKING_ID': getattr(
            settings, 'ANALYTICS_TRACKING_ID', 'UA-XXXXXXX-XX'),
        'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID,
    }
