from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    badge_set = models.ManyToManyField('Badge', related_name='user_set')

    def __repr__(self) -> str:
        return f"Person[{self.name}]"

    def __str__(self) -> str:
        return repr(self)


class Badge(models.Model):
    name = models.CharField(max_length=200)
    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
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
