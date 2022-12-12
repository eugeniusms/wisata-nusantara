from django.shortcuts import render
from daftar_event.models import Event
from daftar_event.forms import event_form
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404

# Create your views here.
def daftar_event(request) :
  daftar_event = Event.objects.all()
  username = request.user.username
  user_admin = username = "aul"
  context = {
    'daftar_event' : daftar_event,
    'username' : username,
    'user_admin' : user_admin,
  }
  return render(request,"daftar_event.html",context)

@login_required(login_url='/auth/login')
@csrf_exempt
def tambah_event(request) :
  form = event_form(request.POST or None)
  context = {
    'forms' : form
  }
  return render(request,'tambah_event.html',context)

def show_json(request) :
  data = Event.objects.all()
  return HttpResponse(serializers.serialize("json",data),content_type="application/json")

@login_required(login_url='/auth/login')
@csrf_exempt
def delete_event(request,id):
  if request.method == 'DELETE' :
    Event.objects.filter(id=id).delete()
  return JsonResponse({"object": "Data dihapus"},status=200)
  
def lihat_event(request, id):
  event = Event.objects.get(pk=id)
  context = {
    'nama': event.nama,
    'lokasi': event.lokasi,
    'jenis': event.jenis,
    'deskripsi' : event.deskripsi,
    'foto' : event.foto,
  }
  return render(request, 'event.html', context)

@login_required(login_url='/auth/login')
@csrf_exempt
def add_json(request):
  if request.method=='POST':
    nama = request.POST.get('nama')
    lokasi = request.POST.get('lokasi')
    jenis = request.POST.get('jenis')
    deskripsi = request.POST.get('deskripsi')
    foto = request.POST.get('foto')
    Event.objects.create(nama=nama, lokasi=lokasi, jenis = jenis, deskripsi=deskripsi,foto=foto)
    return JsonResponse({"Sukses": "Data masuk"},status=200)

def category_event(request,cat):
  data = Event.objects.filter(jenis=cat)
  if cat == "All":
    data = Event.objects.all()
  return HttpResponse(serializers.serialize("json",data),content_type="application/json")

@csrf_exempt
def add_from_flutter(request):
  if request.method == "POST" :
    request_data = json.load(request.body)
    nama = request_data['nama']
    lokasi = request_data['lokasi']
    jenis = request_data['jenis']
    deskripsi = request_data['deskripsi']
    foto = request_data['foto']
    event = Event(
      nama = nama,
      lokasi = lokasi,
      jenis = jenis,
      deskripsi= deskripsi,
      foto = foto,
    )
    event.save()
    return JsonResponse({"Sukses" : "Data masuk"}, status = 200)
  return JsonResponse({"Gagal" : "Data tidak masuk"}, status= 304)

@csrf_exempt() 
def delete_from_flutter(request, id) :
  if request.method == 'DELETE' :
    data = Event.objects.get(id=id)
    post.delete()
    return JsonResponse({"object": "Data dihapus"},status=200)
 