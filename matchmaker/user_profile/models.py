"""Models for the ``user_profile`` app."""
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from registration.signals import user_registered
from social_auth.backends.facebook import FacebookBackend
from social_auth.signals import pre_update, socialauth_registered
from user_profile.constants import GENDER_CHOICES, TIMEZONE_CHOICES


class UserProfile(models.Model):
    """
    Custom user profile. Extends the standart ``User`` model.

    :user: the user this profile belongs to.
    :timezone: the timezone setting of a user.
    :gender: Gender of the user.
    :birthday: Birthday of the user.
    :location: Location of the user.
    :facebook_profile: Facebook profile of the user.

    """
    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
    )

    display_name = models.CharField(
        max_length=256,
        verbose_name=_('Display name'),
        help_text=_(
            'This is the name that shows up when you check-in to a place.'),
        blank=True,
    )

    username = models.SlugField(
        max_length=32,
        verbose_name=_('Username'),
        blank=True,
    )

    timezone = models.CharField(
        max_length=512,
        verbose_name=_('Timezone'),
        choices=TIMEZONE_CHOICES,
        blank=False,
        default='Europe/Berlin',
    )

    gender = models.CharField(
        max_length=32,
        verbose_name=_('Gender'),
        choices=GENDER_CHOICES,
        blank=True,
    )

    birthday = models.DateField(
        verbose_name=_('Birthday'),
        blank=True, null=True,
    )

    location = models.CharField(
        max_length=256,
        verbose_name=_('Location'),
        blank=True,
    )

    facebook_profile = models.CharField(
        max_length=256,
        verbose_name=_('Facebook ID'),
        blank=True,
    )


def create_profile_for_new_user(user):
    """Deletes existing profile and creates a new profile for a new user."""
    UserProfile.objects.filter(user=user).delete()
    UserProfile.objects.create(user=user)


@receiver(user_registered)
def user_registered_handler(sender, user, request, **kwargs):
    """Creates a new profile for a new user registered via email."""
    user.email = user.email.lower()
    user.save()
    create_profile_for_new_user(user)


def new_users_handler(sender, user, response, details, **kwargs):
    """Creates a new profile for a new user registered via social auth."""
    user.email = user.email.lower()
    user.save()
    create_profile_for_new_user(user)
socialauth_registered.connect(new_users_handler, sender=None)


def facebook_extra_values(sender, user, response, details, **kwargs):
    """Adds extra information retrieved from facebook to the profile."""
    try:
        birthday = timezone.datetime.strptime(
            response.get('birthday'), '%m/%d/%Y').date()
    except TypeError:
        birthday = None
    location = response.get('location', '')
    if location:
        location = response['location'].get('name')
    UserProfile.objects.filter(user=user).update(
        gender=response.get('gender', ''),
        location=location,
        facebook_profile=response.get('username', ''),
        birthday=birthday,
    )
    User.objects.filter(pk=user.pk).update(
        first_name=response.get('first_name', ''),
        last_name=response.get('last_name', ''),
    )
    return True
pre_update.connect(facebook_extra_values, sender=FacebookBackend)
