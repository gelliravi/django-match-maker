"""URLs for the ``places`` app."""
from django.conf.urls.defaults import patterns, url

from places.views import CreatePlaceView, PlaceListView


urlpatterns = patterns(
    '',
    url(r'^$',
        PlaceListView.as_view(),
        name='places_list',),

    url(r'^create/$',
        CreatePlaceView.as_view(),
        name='places_create',),
)
