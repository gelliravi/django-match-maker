"""URLs for the ``places`` app."""
from django.conf.urls.defaults import patterns, url

from places.views import PlaceCreateView, PlaceDetailView, PlaceListView


urlpatterns = patterns(
    '',
    url(r'^$',
        PlaceListView.as_view(),
        name='places_list',),

    url(r'^(?P<pk>\d+)/$',
        PlaceDetailView.as_view(),
        name='places_detail',),

    url(r'^create/$',
        PlaceCreateView.as_view(),
        name='places_create',),
)
