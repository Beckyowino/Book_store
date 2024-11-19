from django.shortcuts import render
from .models import Event
from django.http import JsonResponse
from .forms import EventForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
import json

# Create your views here.
def books(request):
    return render(request, 'books.html')

def pricing(request):
    return render(request, 'pricing.html')

def authors(request):
    return render(request, 'authors.html')

def stefan(request):
    return render(request, 'stefan.html')

def virginie(request):
    return render(request, 'virginie.html')

def leo(request):
    return render(request, 'leo.html')

def bram(request):
    return render(request, 'bram.html')

def michelle(request):
    return render(request, 'michelle.html')

def virginia(request):
    return render(request, 'virginia.html')

def charles(request):
    return render(request, 'charles.html')

def kurt(request):
    return render(request, 'kurt.html')

def markus(request):
    return render(request, 'markus.html')

def events(request):
    return render(request, 'events.html')
@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        start_time = parse_datetime(data.get('start'))
        end_time = parse_datetime(data.get('end'))

        if not start_time:
            return JsonResponse({"error": "Start time is required."}, status=400)

        # Save the event to the database
        event = Event.objects.create(
            title=title,
            start_time=start_time,
            end_time=end_time,
            description=data.get('description', ''),
        )

        return JsonResponse({
            "id": event.id,
            "title": event.title,
            "start": event.start_time.isoformat() if event.start_time else None,
            "end": event.end_time.isoformat() if event.end_time else None,
            "description": event.description,
        })

    return JsonResponse({"error": "Invalid request"}, status=400)

def event_json(request):
    myevents = Event.objects.filter(start_time__isnull=False)
    events = [
        {
            "id": event.id,
            "title": event.title,
            "start": event.start_time.isoformat() if event.start_time else None,
            "end": event.end_time.isoformat() if event.end_time else None,
            "description": event.description,
        }
        for event in myevents
    ]
    return JsonResponse(events, safe=False)

@csrf_exempt
def delete_event(request, event_id):
    if request.method == 'DELETE':
        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            return JsonResponse({'message': 'Event deleted successfully!'}, status=200)
        except Event.DoesNotExist:
            return JsonResponse({'error': 'Event not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def save_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        start = request.POST.get('start_time')
        end = request.POST.get('end_time')
        description = request.POST.get('description')

        # Save to the database
        event = Event.objects.create(title=title, start=start, end=end, description=description)
        return JsonResponse({'message': 'Event saved successfully!', 'id': event.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def fetch_events(request):
    events = Event.objects.all().values('id', 'title', 'start_time', 'end_time', 'description')
    return JsonResponse(list(events), safe=False)
