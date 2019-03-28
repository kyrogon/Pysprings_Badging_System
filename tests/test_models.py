from badging.users import models


def test_person_str():
    """A person should pretty print."""
    p = models.Person(name="Alice")
    assert str(p) == "Person[Alice]"
