from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Destinasi
import json


# Create your views here.
def daftar_destinasi(request):
  return render(request, 'daftar-destinasi.html')

@csrf_exempt
def tambah_destinasi(request):
  if (request.method == 'POST'):
    nama = request.POST.get('nama')
    deskripsi = request.POST.get('deskripsi')
    lokasi = request.POST.get('lokasi')
    kategori = request.POST.get('kategori')

    destinasi = Destinasi(
      nama=nama,
      deskripsi=deskripsi,
      lokasi=lokasi,
      kategori=kategori
    )
    destinasi.save()

    context = {
      'nama': destinasi.nama,
      'description': destinasi.deskripsi,
      'location': destinasi.lokasi,
      'category': destinasi.kategori
    }

    print(context)

    return JsonResponse({"header": "Destinasi Ditambahkan"}, status=200)

  return render(request, 'tambah-destinasi.html')


# def add(request):
  