"""
Configure the environment for testing.
"""
import os
import sys
import django

# TODO: Remove this if we fix the folder structure.  # pylint: disable=fixme
# We only need this because the base app folder (where `manage.py` is) is not
# where we run the tests.
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "badging.settings")


def pytest_configure():
    django.setup()
