"""Admin classes for the ``places`` app."""
from django.conf import settings
from django.contrib.gis import admin

from places.models import Place, PlaceType


class GoogleMapsAdmin(admin.OSMGeoAdmin):
    map_template = 'gis/admin/google.html'
    extra_js = [
        'https://maps.google.com/'
        'maps?file=api&v=3&sensor=false&callback=initialize&key={0}'.format(
            settings.GOOGLE_MAPS_API_KEY),
    ]


admin.site.register(Place, GoogleMapsAdmin)
admin.site.register(PlaceType)
