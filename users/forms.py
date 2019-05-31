from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.Person
        exclude = []


class BadgeForm(forms.ModelForm):
    class Meta:
        model = models.Badge
        exclude = []
