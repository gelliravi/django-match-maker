"""Forms for the ``checkins`` app."""
from django import forms
from django.conf import settings
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _

from checkins.models import Checkin
from places.forms import FormWithLatLngMixin


class CheckinCreateForm(FormWithLatLngMixin, forms.Form):
    """Form that creates a Checkin object."""
    access_token = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    post_to_facebook = forms.BooleanField(
        label=_('Post to Facebook'),
        required=False,
    )

    class Media:
        css = {
            'all': ('css/libs/iphone_checkbox/style.css', ),
        }
        js = ('js/libs/iphone-style-checkboxes.js', )

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
        Creates a new ``Checkin`` for a user.

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

        from matchmaker import facebook
        if (self.cleaned_data.get('access_token')
                and self.cleaned_data.get('post_to_facebook')):
            graph = facebook.GraphAPI(self.cleaned_data.get('access_token'))
            graph.put_wall_post(
                "I'm playing basketball now at {0}."
                ' Come and join me: {1}{2}'.format(
                    self.place, settings.HOSTNAME,
                    self.place.get_absolute_url()
            ))
        return checkin


class CheckinMassCreateForm(FormWithLatLngMixin, forms.Form):
    """Form that creates a number of anonymous checkins."""
    count = forms.IntegerField(
        label=_('Count'),
        min_value=1,
        max_value=12,
    )

    def __init__(self, user=None, place=None, user_name_base='User', *args,
                 **kwargs):
        super(CheckinMassCreateForm, self).__init__(*args, **kwargs)
        assert place is not None, ('Place cannot be None.')
        self.place = place
        self.user_name_base = user_name_base
        self.add_lat_lng_fields()

    def _get_highest_user_name(self):
        """
        Returns the highest username amongst the currently checked in users.

        This can happen if someone checked in 5 anonymous users. Then someone
        else checks in another 5 users. These last 5 users should be named
        ``User6`` to ``User10``.

        """
        checkins = Checkin.objects.filter(place=self.place, expired=False)
        highest_number = 0
        for checkin in checkins:
            if checkin.user_name.startswith(self.user_name_base):
                try:
                    current_number = int(checkin.user_name.replace(
                        self.user_name_base, ''))
                except ValueError:
                    # Someone has named himself something like ``UserA``
                    current_number = 0
                if current_number > highest_number:
                    highest_number = current_number
        return highest_number

    def pre_save(self, *args, **kwargs):
        """Can be overridden by forms inheriting this form."""
        return

    def save(self, *args, **kwargs):
        """
        Creates a number of new checkins for anonymous users.

        Users will be called ``User1``, ``User2`` and so on.

        """
        self.pre_save(*args, **kwargs)
        highest_number = self._get_highest_user_name()
        count = self.cleaned_data.get('count')
        for i in range(highest_number + 1, highest_number + 1 + count, 1):
            checkin = Checkin()
            checkin.place = self.place
            checkin.user_name = '{0}{1}'.format(self.user_name_base, i)
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
