from django import forms
from . import models


class NewBadgeForm(forms.ModelForm):
    class Meta:
        model = models.Badge
        exclude = []
