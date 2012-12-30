"""Forms for the ``matchmaker`` project."""
from django.utils.translation import ugettext_lazy as _

from checkins.forms import CheckinCreateForm


class CustomCheckinCreateForm(CheckinCreateForm):
    def __init__(self, user=None, *args, **kwargs):
        """
        Adds a `user_name` field to the form if needed.

        It is needed if the user is anonymous or if the user has not yet
        saved a display name.

        """
        super(CustomCheckinCreateForm, self).__init__(
            user=user, *args, **kwargs)
        if 'user_name' in self.fields:
            return
        if self.user and not self.user.get_profile().display_name:
            help_text = _(
                'Select a display name that appears on this court while you'
                ' are checked in. Your prename would usually be a good choice.'
                ' You only have to set this once.'
            )
            self._add_user_name_field(help_text=help_text)

    def pre_save(self, *args, **kwargs):
        """
        Saves the user's display name.

        Therefore, after naming himself at the first check-in he does not have
        to re-enter the display name again.

        """
        super(CustomCheckinCreateForm, self).pre_save(*args, **kwargs)
        if self.user and 'user_name' in self.cleaned_data:
            profile = self.user.get_profile()
            profile.display_name = self.cleaned_data['user_name']
            profile.save()
