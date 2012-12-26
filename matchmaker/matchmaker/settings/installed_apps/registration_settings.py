"""Registration related settings."""

AUTHENTICATION_BACKENDS = (
    'registration_email.auth.EmailBackend',
)

LOGIN_REDIRECT_URL = '/places/'
REGISTRATION_EMAIL_REGISTER_SUCCESS_URL = LOGIN_REDIRECT_URL
