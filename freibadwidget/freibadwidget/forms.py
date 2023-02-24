from django import forms

from .models import ManualOpenCloseEvent


class OpenCloseForm(forms.ModelForm):

    class Meta:
         model = ManualOpenCloseEvent
         fields = ("event_type")
