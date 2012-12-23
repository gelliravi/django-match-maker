"""Admin classes for the ``places`` app."""
from django.contrib.gis import admin

from places.models import Place, PlaceType


admin.site.register(Place, admin.GeoModelAdmin)
admin.site.register(PlaceType)
