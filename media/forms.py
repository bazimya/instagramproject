from.models import user
from django import forms


class Formprofile(forms.ModelForm):
    class Meta:
        model = user
        exclude = ['curentus']