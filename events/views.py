from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from events.models import Events
from django.forms.models import model_to_dict
from django.utils import timezone

from events.serializers.event_serializers import EventsSerializer


@csrf_exempt
@require_POST
def create_event(request):
    """Creates an Event Object"""
    event_object = json.loads(request.body)
    event_name = event_object.get("event_name", None)
    starting_time = event_object.get("starting_time", None)
    duration = int(event_object.get("duration", 0))

    if not event_name:
        return Response(data={"success": False,
                              "error": "Event name is required key"}
                        )

    if not starting_time:
        return Response(data={"success": False,
                              "error": "Starting time is required key"}
                        )
    if not duration:
        return Response(data={"success": False,
                              "error": "Duration is required key"}
                        )

    date_time = datetime.strptime(starting_time, '%d/%m/%y %H:%M:%S')
    if date_time.date() < timezone.now().date():
        return Response(data={"success": False,
                              "error": "Starting time can not be in past"}
                        )

    new_event = Events.objects.create(
        name=event_name,
        starting_time=date_time,
        duration=duration
    )

    event = EventsSerializer(new_event, many=False)
    return Response(data={"success": True, "event": event.data})


@csrf_exempt
@require_GET
def list_events(request):
    upcoming_events = []
    live_events = []
    duration = timezone.now() - timedelta(hours=0, minutes=10)
    for event in Events.objects.all():
        if timezone.now() <= event.starting_time <= duration:
            live_events.append(event)
        else:
            upcoming_events.append(event)

    live_events = EventsSerializer(live_events, many=True)
    upcoming_events = EventsSerializer(upcoming_events, many=True)

    return Response(data={"upcoming_events": upcoming_events.data, "live_events": live_events.data})


@csrf_exempt
@api_view(['GET', 'POST'])
def events(request):
    if request.method == 'GET':
        return list_events(request)
    elif request.method == 'POST':
        return create_event(request)
