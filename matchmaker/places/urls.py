"""URLs for the ``places`` app."""
from django.conf.urls.defaults import patterns, url

from places.views import CreatePlaceView


urlpatterns = patterns(
    '',
    url(r'^create/$',
        CreatePlaceView.as_view(),
        name='places_create',),
)
