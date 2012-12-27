"""Test settings for the project."""
from matchmaker.settings import *  # NOQA


PREPEND_WWW = False

INSTALLED_APPS += [
    'django_nose',
    'subscriptions.tests.test_app',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': ':memory:',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


EMAIL_SUBJECT_PREFIX = '[test] '
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
SOUTH_TESTS_MIGRATE = False


TEST_RUNNER = 'django_libs.testrunner.NoseCoverageTestRunner'
COVERAGE_MODULE_EXCLUDES = [
    'admin.py$',
    'django_extensions',
    'fixtures',
    'migrations',
    'settings$',
    'tests$',
    'urls$',
    'wsgi.py$',
    'locale$',
]
COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS
COVERAGE_MODULE_EXCLUDES += DJANGO_APPS
COVERAGE_REPORT_HTML_OUTPUT_DIR = "coverage"
