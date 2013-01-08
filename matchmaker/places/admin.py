"""Admin classes for the ``places`` app."""
from django.conf import settings
from django.contrib.gis import admin

from places.models import Place, PlaceType


class GoogleMapsAdmin(admin.OSMGeoAdmin):
    map_template = 'gis/admin/google.html'
    extra_js = [
        'https://maps.googleapis.com/'
        'maps/api/js?key={0}&sensor=false'.format(
            settings.GOOGLE_MAPS_API_KEY),
    ]


admin.site.register(Place, GoogleMapsAdmin)
admin.site.register(PlaceType)
