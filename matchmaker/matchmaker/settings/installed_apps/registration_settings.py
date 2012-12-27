"""django-registration and django-social-auth related settings."""

AUTHENTICATION_BACKENDS = (
    'registration_email.auth.EmailBackend',
    'social_auth.backends.facebook.FacebookBackend',
)

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/places/'
LOGIN_ERROR_URL = '/accounts/login-error/'
REGISTRATION_EMAIL_REGISTER_SUCCESS_URL = LOGIN_REDIRECT_URL

SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'matchmaker.pipeline.user.get_username',
    'matchmaker.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details'
)

FACEBOOK_EXTENDED_PERMISSIONS = [
    'email', 'user_birthday', 'user_location', ]
