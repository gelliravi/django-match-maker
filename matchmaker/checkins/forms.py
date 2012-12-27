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
            self._add_user_name_field()
        self.add_lat_lng_fields()

    def _add_user_name_field(self, help_text=None):
        if help_text is None:
            help_text = _(
                'Give yourself a nickanme, or even better,'
                ' <a href="/accounts/register/">create an account</a>'
            ),

        self.fields['user_name'] = forms.CharField(
            max_length=256,
            label=_('Your name'),
            help_text=help_text,
        )

    def pre_save(self, *args, **kwargs):
        """Can be overridden by forms inheriting this form."""
        return

    def save(self, *args, **kwargs):
        """
        Creates a new ``Checkin`` for.

        This can be done for anonymous users or for real users.
        Since we call ``checkin.save()`` here, the ``save()`` override will
        take care of expiring older checkins for the given user.

        """
        self.pre_save(*args, **kwargs)
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


class CheckoutForm(forms.Form):
    """Form that expires the user's check-ins."""
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CheckoutForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        """Expires all checkins for the given user."""
        Checkin.objects.filter(user=self.user).update(expired=True)
