"""Admin classes for the ``places`` app."""
from django.contrib.gis import admin

from places.models import Place, PlaceType


class GoogleAdmin(admin.OSMGeoAdmin):
    map_template = 'gis/admin/google.html'
    extra_js = [
        'https://maps.google.com/maps?file=api&v=3&sensor=false&callback=initialize']


admin.site.register(Place, GoogleAdmin)
admin.site.register(PlaceType)
