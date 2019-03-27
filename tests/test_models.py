import django
from django.test import TestCase

django.setup()

from badging.users import models  # pylint: disable=wrong-import-position # isort:skip


def test_person_str():
    """A person should pretty print."""
    p = models.Person(name="Alice")
    assert str(p) == "Person[Alice]"
