from django.contrib import admin
from events.models import Events


class EventsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "starting_time",
        "event_duration",
    ]

    def event_duration(self, obj=None):
        return f"{obj.duration} minutes"


admin.site.register(Events, EventsAdmin)
