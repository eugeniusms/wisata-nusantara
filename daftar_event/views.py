from django.shortcuts import render
from daftar_event.models import Event

# Create your views here.
def daftar_event(request) :
  daftar_event = Event.objects.all()
  context = {
    'daftar_event' : daftar_event
  }
  return render(request,"daftar_event.html",context)