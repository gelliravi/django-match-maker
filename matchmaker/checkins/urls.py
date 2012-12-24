"""URLs for the ``checkins`` app."""
from django.conf.urls.defaults import patterns, url

from checkins.views import CheckinCreateView


urlpatterns = patterns(
    '',
    url(r'^create/(?P<place_pk>\d+)/$',
        CheckinCreateView.as_view(),
        name='checkins_create',),
)
