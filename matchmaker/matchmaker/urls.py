from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django_libs.views import RapidPrototypingView

from checkins.views import CheckinCreateView
from matchmaker.forms import CustomCheckinCreateForm
from matchmaker.views import (
    HomeView,
    CustomPlaceDetailView,
    CustomPlaceListView,
)


admin.autodiscover()

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG is False and settings.SANDBOX is True:
    # This helps if you set `DEBUG = False` locally. This way you don't need
    # to setup a webserver in order to get 404, 500 pages and media files
    # served.
    urlpatterns += patterns('',
        (r'^404/$', 'django.views.defaults.page_not_found'),
        (r'^500/$', 'django.views.defaults.server_error'),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/', include('api.urls')),
    url(r'^places/$',
        CustomPlaceListView.as_view(),
        name='places_list',),
    url(r'^places/(?P<pk>\d+)/$',
        CustomPlaceDetailView.as_view(),
        name='places_detail',),
    url(r'^places/', include('places.urls')),
    url(r'^checkins/create/(?P<place_pk>\d+)/$',
        CheckinCreateView.as_view(
            form_class=CustomCheckinCreateForm,
        ),
        name='checkins_create',),
    url(r'^checkins/', include('checkins.urls')),
    url(r'^subscribe/', include('subscribe.urls')),
    url(r'^accounts/', include('registration_email.backends.simple.urls')),
    url(r'^accounts/', include('social_auth.urls')),
    url(r'^profile/', include('user_profile.urls')),
    url(r'^umedia/', include('user_media.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prototype/(?P<template_path>.*)$',
        RapidPrototypingView.as_view(),
        name='prototype'),
)
