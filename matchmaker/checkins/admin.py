"""Admin classes for the ``checkins`` app."""
from django.contrib.gis import admin

from checkins.models import Checkin


admin.site.register(Checkin, admin.GeoModelAdmin)
