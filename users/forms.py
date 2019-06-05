from django import forms
from . import models


class BadgeForm(forms.ModelForm):
    class Meta:
        model = models.Badge
        exclude = []
