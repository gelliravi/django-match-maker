from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_libs.views import RapidPrototypingView

from checkins.views import CheckinCreateView
from matchmaker.forms import CustomCheckinCreateForm
from matchmaker.views import (
    HomeView,
    CustomPlaceDetailView,
    CustomPlaceListView,
)


admin.autodiscover()


urlpatterns = patterns(
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
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prototype/(?P<template_path>.*)$',
        RapidPrototypingView.as_view(),
        name='prototype'),
)
