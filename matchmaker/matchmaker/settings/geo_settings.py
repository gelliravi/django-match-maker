"""Geolocation related settings."""
import os

from matchmaker.settings.base_settings import PROJECT_ROOT


GEOIP_PATH = os.path.join(PROJECT_ROOT, 'matchmaker/geoip/datasets')
