"""URLs for the ``api`` app."""
from django.conf.urls.defaults import patterns, url

from api.views import UserCountAPIView


urlpatterns = patterns(
    '',
    url(r'^v1/users/count/$',
        UserCountAPIView.as_view(),
        name='api_user_count',),
)
