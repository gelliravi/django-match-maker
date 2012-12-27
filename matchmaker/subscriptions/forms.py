"""Forms for the ``subscriptions`` app."""
from django import forms
from django.contrib.contenttypes.models import ContentType

from subscriptions.models import Subscription


class SubscriptionCreateForm(forms.Form):
    def __init__(self, user, content_object, *args, **kwargs):
        self.user = user
        self.content_object = content_object
        self.ctype = ContentType.objects.get_for_model(self.content_object)
        super(SubscriptionCreateForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        """Adds a subscription for the given user to the given object."""
        method_kwargs = {
            'user': self.user,
            'content_type': self.ctype,
            'object_id': self.content_object.pk,
        }
        try:
            subscription = Subscription.objects.get(**method_kwargs)
        except Subscription.DoesNotExist:
            subscription = Subscription.objects.create(**method_kwargs)
        return subscription
