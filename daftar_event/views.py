from django.shortcuts import render, get_object_or_404
from daftar_event.models import Event
from daftar_event.forms import event_form
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.
def daftar_event(request) :
  daftar_event = Event.objects.all()
  context = {
    'daftar_event' : daftar_event
  }
  return render(request,"daftar_event.html",context)

@csrf_exempt
def tambah_event(request) :
  form = event_form(request.POST or None)

  if form.is_valid() and request.method=='POST':
        form.save()
        return HttpResponseRedirect('/daftar-event/')
  else:
    context = {
      'forms' : form
    }
    return render(request,'tambah_event.html',context)
    
def show_json(request) :
  data = Event.objects.all()
  return HttpResponse(serializers.serialize("json",data),content_type="application/json")

def delete_task(request,id):
  event = Event.objects.get(id=id)
  event.delete()
  return redirect('daftar_event:daftar_event')

def lihat_event(request, id):
  event = Event.objects.get(pk=id)
  context = {
    'nama': event.nama,
    'lokasi': event.lokasi,
    'jenis': event.jenis,
    'deskripsi' : event.deskripsi,
  }
  return render(request, 'event.html', context)


