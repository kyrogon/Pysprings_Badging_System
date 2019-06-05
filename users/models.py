from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    # badge_set = models.ManyToManyField('Badge', related_name='user_set')

    class Meta:
        verbose_name_plural = 'People'

    def __repr__(self) -> str:
        return f"Person[{self.name}]"

    def __str__(self) -> str:
        return repr(self)


class Badge(models.Model):
    name = models.CharField(max_length=200)
    presenter = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateField(auto_now=True)
    user_set = models.ManyToManyField('Person', related_name='badge_set')

    class Meta:
        unique_together = ('name', 'presenter')

    def user_count(self):
        return len(self.user_set.all())

    def __repr__(self) -> str:
        return (
            f"Badge[name={self.name}, presenter={self.presenter}]"
        )

    def __str__(self) -> str:
        return repr(self)
