from django.conf.urls import patterns, include, url

from django.contrib import admin

from matchmaker.views import HomeView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^places/', include('places.urls')),
    url(r'^checkins/', include('checkins.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
