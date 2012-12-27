from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_libs.views import RapidPrototypingView

from matchmaker.views import HomeView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^places/', include('places.urls')),
    url(r'^checkins/', include('checkins.urls')),
    url(r'^subscriptions/', include('subscriptions.urls')),
    url(r'^accounts/', include('registration_email.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prototype/(?P<template_path>.*)$',
        RapidPrototypingView.as_view(),
        name='prototype'),
)
