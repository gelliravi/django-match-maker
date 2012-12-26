"""URLs for the ``checkins`` app."""
from django.conf.urls.defaults import patterns, url

from checkins.views import CheckinCreateView, CheckoutView


urlpatterns = patterns(
    '',
    url(r'^create/(?P<place_pk>\d+)/$',
        CheckinCreateView.as_view(),
        name='checkins_create',),

    url(r'^checkout/$',
        CheckoutView.as_view(),
        name='checkins_checkout',),
)
