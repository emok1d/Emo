from django.shortcuts import render
from .models import Event
from django.views import View


# Create your views here.
class EventView(View):
    def get(self, request, *args, **kwargs):
        event = Event.objects.all()
        return render(request, "events/index.html", context={"event": event})
