import django
from django.test import TestCase

django.setup()

from badging.users import models # isort:skip

class TestModels(TestCase):
    def test_person_str(self):
        """A person should pretty print."""
        p = models.Person(name='Alice')
        assert str(p) == 'Person[Alice]'
