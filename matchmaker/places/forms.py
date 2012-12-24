"""Forms for the ``places`` app."""
from django import forms
from django.contrib.gis.geos import Point

from places.models import Place


class PlaceCreateForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ['point', ]

    def __init__(self, *args, **kwargs):
        super(PlaceCreateForm, self).__init__(*args, **kwargs)
        self.fields['lat'] = forms.FloatField(
            widget=forms.HiddenInput(),
        )
        self.fields['lng'] = forms.FloatField(
            widget=forms.HiddenInput(),
        )

    def save(self, *args, **kwargs):
        assert hasattr(self, 'cleaned_data'), (
            'Please call `is_valid` before calling `save`')
        self.instance.point = Point(
            self.cleaned_data['lng'], self.cleaned_data['lat'])
        return super(PlaceCreateForm, self).save(*args, **kwargs)
