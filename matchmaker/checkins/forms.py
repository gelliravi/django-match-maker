"""Forms for the ``checkins`` app."""
from django import forms
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _

from checkins.models import Checkin
from places.forms import FormWithLatLngMixin


class CheckinCreateForm(FormWithLatLngMixin, forms.Form):
    """Form that creates a Checkin object."""
    def __init__(self, user=None, place=None, *args, **kwargs):
        super(CheckinCreateForm, self).__init__(*args, **kwargs)
        assert place is not None, ('Place cannot be None.')
        self.place = place
        if user:
            self.user = user
        else:
            self.user = None
            self.fields['user_name'] = forms.CharField(
                max_length=256,
                label=_('Your name'),
            )
        self.add_lat_lng_fields()

    def save(self, *args, **kwargs):
        checkin = Checkin()
        checkin.place = self.place
        if self.user:
            checkin.user = self.user
        else:
            checkin.user_name = self.cleaned_data['user_name']
        checkin.point = Point(
            self.cleaned_data['lng'],
            self.cleaned_data['lat'],
        )
        checkin.save()
        return checkin
