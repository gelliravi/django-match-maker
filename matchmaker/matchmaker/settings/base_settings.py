"""
Settings that might be useful in our other settings-files.

"""
import os


DEBUG = False
TEMPLATE_DEBUG = DEBUG


# The folder where ./manage.py resides.
PROJECT_ROOT = os.path.realpath(
    os.path.join(os.path.dirname(__file__), '../..'))
