"""Fabric tasks for local development."""
from django.conf import settings

from fabric.api import local

from development_fabfile.fabfile.local import test as test_orig


def create_database():
    """Creates the local database."""
    local('psql -h localhost -c "CREATE DATABASE {0}"'.format(
        settings.PROJECT_NAME))
    local('psql -h localhost matchmaker -c "CREATE EXTENSION postgis"')
    local('psql -h localhost -c "GRANT ALL PRIVILEGES ON DATABASE {0}'
          ' to {0}"'.format(settings.PROJECT_NAME))
    local('psql -h localhost matchmaker -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {0}"'.format(settings.PROJECT_NAME))


def drop_database():
    """Drops the local database."""
    local('psql -h localhost -c "DROP DATABASE {0}"'.format(
        settings.PROJECT_NAME))


def test(options=None, integration=1,
         settings='matchmaker.settings.test_settings'):
    return test_orig(options, integration, settings)


def rebuild():
    """Deletes and re-creates the local database."""
    drop_database()
    create_database()
    local('python2.7 manage.py syncdb --noinput')
    local('python2.7 manage.py migrate')
