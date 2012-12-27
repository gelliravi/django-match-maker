"""URLs for the ``subscriptions`` app."""
from django.conf.urls.defaults import patterns, url

from subscriptions.views import SubscriptionCreateView


urlpatterns = patterns(
    '',
    url(r'^create/(?P<ctype_pk>\d+)/(?P<object_pk>\d+)/$',
        SubscriptionCreateView.as_view(),
        name='subscriptions_create',),
)
