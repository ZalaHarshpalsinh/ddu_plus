from django import forms
from events.models import *

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'poster', 'description', 'dateTime', 'venue']




