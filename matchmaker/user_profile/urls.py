"""URLs for the ``user_profile`` app."""
from django.conf.urls.defaults import patterns, url

from user_profile.views import UsernameUpdateView, UserProfileUpdateView


urlpatterns = patterns(
    '',
    url(r'^$',
        UserProfileUpdateView.as_view(),
        name='user_profile_update', ),

    url(r'^username/$',
        UsernameUpdateView.as_view(),
        name='user_profile_username_update', ),

)
