"""Admin classes for the ``subscriptions`` app."""
from django.contrib import admin

from subscriptions.models import Subscription


admin.site.register(Subscription)
