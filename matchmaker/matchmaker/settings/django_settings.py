# Django settings for matchmaker project.

# Override this in your local_settings.py on the server.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.  # nopep8
        'NAME': 'matchmaker',                      # Or path to database file if using sqlite3.  # nopep8
        'USER': 'matchmaker',                      # Not used with sqlite3.  # nopep8
        'PASSWORD': 'matchmaker',                  # Not used with sqlite3.  # nopep8
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.  # nopep8
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.  # nopep8
    }
}

SITE_ID = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*h(0jul7hrxo1tmg*brce!p3(9cn8bu!(ia&amp;1fbl_qbj05(-!@'

ROOT_URLCONF = 'matchmaker.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'matchmaker.wsgi.application'
