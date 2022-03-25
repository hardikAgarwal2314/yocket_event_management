import os

from django import forms
from django.core.exceptions import ValidationError


class CreateEventForm(forms.Form):
    def __init__(self, event_object, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_name = event_object.get("event_name", None)
        self.starting_time = event_object.get("starting_time", None)
        self.duration = event_object.get("duration", None)


    def clean(self, data=None, *args, **kwargs):
        c = self.cleaned_data
        if not self.event_name:
            raise self.errors("Event name is a required key.")
        if not self.starting_time:
            raise ValueError("Event starting time is a required key.")
        if not self.duration:
            raise self.has_error("Event duration is a required key.")
        return c


    def save(self):
        """Update the user profile picture."""
        uploaded_file = self.upload["file"]
        user = self.user
        user.profile_picture = self.user.profile_picture_path(uploaded_file.name)
        user.save(update_fields=["profile_picture"])
