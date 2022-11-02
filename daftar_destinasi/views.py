from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from matplotlib import use
from .models import Destinasi, Suka
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
def hapus_destinasi_by_id(request, id):
  if (request.user.username == "admin"): # hanya user dengan username ini yg bisa hapus destination
    task = Destinasi.objects.get(pk=id)
    task.delete()
  return HttpResponseRedirect("/destination/")

def show_suka_json(request):
  data = Suka.objects.all()
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
@login_required(login_url='/auth/login')
def sukai_destinasi(request, id):
  user = request.user
  data = Destinasi.objects.get(pk=id)
  suka = Suka(user=user, destinasi=data)

  # jika belum pernah ada maka disave (menjamin unique) 
  # menyimpan object Suka
  if (Suka.objects.filter(user=user, destinasi=data).count() == 0):
    suka.save()

    # menambahkan jumlah suka di Destinasi
    data.jumlah_suka += 1
    data.save()

  return HttpResponseRedirect("/destination/")

@login_required(login_url='/auth/login')
def show_wishlist(request):
  user = request.user
  data = Suka.objects.filter(user=user)
  return render(request, 'wishlist.html', {'data': data})