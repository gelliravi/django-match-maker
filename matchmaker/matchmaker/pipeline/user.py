"""Custom pipelines for ``django-social-auth``."""
from django.contrib.auth.models import User

from registration_email.forms import generate_username
from social_auth.models import UserSocialAuth


def create_user(backend, details, response, uid, username, user=None, *args,
                **kwargs):
    """
    Creates a user. Depends on get_username pipeline.

    If a user with this email already exists, we return that user.

    """
    if user:
        return {'user': user}
    if not username:
        return None

    args = {'username': username}
    if details.get('email'):
        args['email'] = details['email']

    try:
        user = User.objects.get(username=username)
        is_new = False
    except User.DoesNotExist:
        user = UserSocialAuth.create_user(**args)
        is_new = True

    return {
        'user': user,
        'is_new': is_new,
    }


def get_username(details, user=None, user_exists=None, *args, **kwargs):
    """
    Returns an username for a new user or current username for existing user.

    Makes sure that the username is generated in the same way as we do it
    with ``django-registration-email``.

    """
    email = details['email']

    if user:
        username = user.username
    else:
        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            username = generate_username(email)
    return {'username': username, }
