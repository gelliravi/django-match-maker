"""Forms of the ``user_profile`` app."""
from django import forms

from user_profile.models import UserProfile


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'birthday', 'location', 'facebook_profile', )

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
