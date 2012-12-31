"""Forms of the ``user_profile`` app."""
from django import forms
from django.utils.translation import ugettext_lazy as _

from user_profile.models import UserProfile


class UsernameUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', )

    def clean_username(self):
        data = self.cleaned_data['username']
        try:
            UserProfile.objects.get(username=data)
            raise forms.ValidationError(_(
                'Sorry, this username is already taken.'))
        except UserProfile.DoesNotExist:
            pass
        return data


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('display_name', 'timezone', 'gender', )
