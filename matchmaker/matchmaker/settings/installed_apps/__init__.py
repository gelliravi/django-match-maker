"""
INSTALLED_APPS related settings.

We are splitting up INSTALLED_APPS because we only want to test our own
internal apps.

"""
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.gis',
]

EXTERNAL_APPS = [
    'django_extensions',
    'south',
]

INTERNAL_APPS = []

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS
