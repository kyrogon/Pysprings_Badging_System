from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return f"Person[{self.name}]"

    def __str__(self) -> str:
        return repr(self)


class Badge(models.Model):
    name = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    presenter = models.CharField(max_length=200)

    def __repr__(self) -> str:
        return (
            f"Badge[name={self.name}, person={self.person}, "
            f"presenter={self.presenter}]"
        )

    def __str__(self) -> str:
        return repr(self)