from django import forms

from Student_project_AMMB.events.models import Event


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'