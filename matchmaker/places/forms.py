"""Forms for the ``places`` app."""
from django import forms
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _

from places.models import Place, PlaceType


class FormWithLatLngMixin(object):
    def add_lat_lng_fields(self):
        self.fields['lat'] = forms.FloatField(
            widget=forms.HiddenInput(),
        )
        self.fields['lng'] = forms.FloatField(
            widget=forms.HiddenInput(),
        )


class PlaceCreateForm(FormWithLatLngMixin, forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', ]

    def __init__(self, user=None,  *args, **kwargs):
        super(PlaceCreateForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['name'].help_text = _(
            'Chose a name that is common among players. Usually a nearby'
            ' block, school or park would identify a playing field nicely.')
        self.add_lat_lng_fields()

    def save(self, *args, **kwargs):
        assert hasattr(self, 'cleaned_data'), (
            'Please call `is_valid` before calling `save`')
        if self.user.is_authenticated():
            self.instance.created_by = self.user
        self.instance.point = Point(
            self.cleaned_data['lng'], self.cleaned_data['lat'])
        self.instance.type = PlaceType.objects.get(name='Basketball')
        return super(PlaceCreateForm, self).save(*args, **kwargs)
