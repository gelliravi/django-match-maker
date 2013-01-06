# flake8: noqa
"""Splitting up the ``settings.py`` into several smaller files."""
from matchmaker.settings.base_settings import *
from matchmaker.settings.installed_apps import *
from matchmaker.settings.middleware_settings import *
from matchmaker.settings.template_settings import *
from matchmaker.settings.staticfiles_settings import *
from matchmaker.settings.logging_settings import *
from matchmaker.settings.i18n_settings import *
from matchmaker.settings.email_settings import *
from matchmaker.settings.geo_settings import *
from matchmaker.settings.django_settings import *
from matchmaker.settings.fabfile_settings import *
from matchmaker.settings.local.local_settings import *
