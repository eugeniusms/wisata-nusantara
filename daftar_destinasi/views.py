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

# Create your views here.
def show_json(request):
  data = Destinasi.objects.all()
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def daftar_destinasi(request):
  return render(request, 'daftar-destinasi.html')

@csrf_exempt
@login_required(login_url='/auth/login')
def tambah_destinasi(request):
  if (request.method == 'POST'):
    # nama = request.POST.get('nama')
    # deskripsi = request.POST.get('deskripsi')
    # lokasi = request.POST.get('lokasi')
    # kategori = request.POST.get('kategori')
    # foto_thumbnail_url = request.POST.get('foto_thumbnail_url')
    # foto_cover_url = request.POST.get('foto_cover_url')
    # maps_url = request.POST.get('maps_url')
    # created_by = request.user
    destinasi_form = AddDestinasiForm(request.POST, instance=request.user)

    if destinasi_form.is_valid():
      destinasi_form.save()
      return redirect('daftar_destinasi:daftar_destinasi')
    return redirect('daftar_destinasi:daftar_destinasi')
    # destinasi = Destinasi(
    #   nama=nama,
    #   deskripsi=deskripsi,
    #   lokasi=lokasi,
    #   kategori=kategori,
    #   foto_thumbnail_url=foto_thumbnail_url,
    #   foto_cover_url=foto_cover_url,
    #   maps_url=maps_url,
    #   created_by=created_by
    # )
    # destinasi.save()

    return JsonResponse({"header": "Destinasi Ditambahkan"}, status=200)
  else:
    destinasi_form = AddDestinasiForm()

  context = {
    'destinasi_form': destinasi_form
  }

  return render(request, 'tambah-destinasi.html', context)

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