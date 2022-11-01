from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from matplotlib import use
from .models import Destinasi
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .forms import AddDestinasiForm
from . import forms

# Create your views here.
def show_json(request):
  data = Destinasi.objects.all()
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def daftar_destinasi(request):
  if request.method == "POST":
    form = AddDestinasiForm(request.POST)
    print(form)
    if form.is_valid():
        destinasi = Destinasi(
            nama = form.cleaned_data['nama'],
            deskripsi = form.cleaned_data['deskripsi'],
            lokasi = form.cleaned_data['lokasi'],
            kategori = form.cleaned_data['kategori'],
            foto_thumbnail_url = form.cleaned_data['foto_thumbnail_url'],
            foto_cover_url = form.cleaned_data['foto_cover_url'],
            maps_url = form.cleaned_data['maps_url'],
            created_by = request.user
        )
        # Memasukkan task ke database
        destinasi.save()
        return HttpResponseRedirect("/destination/")
  else:
    form = AddDestinasiForm()
  return render(request, 'daftar-destinasi.html')

@csrf_exempt
@login_required(login_url='/auth/login')
def hapus_destinasi(request):
  if (request.user.username == "eugenius.mario"): # hanya user dengan username ini yg bisa hapus destination
    data = Destinasi.objects.all()

    context = {
      'data': data
    }

    return render(request, 'hapus-destinasi.html', context)
  
@csrf_exempt
@login_required(login_url='/auth/login')
def hapus_destinasi_by_id(request, id):
  if (request.user.username == "eugenius.mario"): # hanya user dengan username ini yg bisa hapus destination
    task = Destinasi.objects.get(pk=id)
    task.delete()
  return HttpResponseRedirect("/destination/delete")