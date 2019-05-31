from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return f"Person[{self.name}]"

    def __str__(self) -> str:
        return repr(self)


class Badge(models.Model):
    name = models.CharField(max_length=200)
    user_set = models.ManyToManyField(
        'Person',
        related_name='badge_set',
        blank=True,
    )
    presenter = models.CharField(max_length=200)

    class Meta:
        unique_together = ('name', 'presenter')

    def __repr__(self) -> str:
        return (
            f"Badge[name={self.name}, presenter={self.presenter}]"
            # f"presenter={self.presenter}]"
        )

    def __str__(self) -> str:
        return repr(self)
