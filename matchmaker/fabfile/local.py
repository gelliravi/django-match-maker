"""Fabric tasks for local development."""
from development_fabfile.fabfile.local import test as test_orig


def test(options=None, integration=1,
         settings='matchmaker.settings.test_settings'):
    return test_orig(options, integration, settings)
