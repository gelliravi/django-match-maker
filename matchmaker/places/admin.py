"""Admin classes for the ``places`` app."""
from django.contrib.gis import admin

from places.models import Place


admin.site.register(Place, admin.GeoModelAdmin)
