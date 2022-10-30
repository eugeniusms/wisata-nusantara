from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from panduan_perjalanan.models import TujuanPerjalanan
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def panduan_perjalanan(request):
  # TujuanPerjalanan.objects.all().delete()
  return render(request, "panduan-perjalanan.html")

def get_perjalanan_json(request):
  daftar_perjalanan = TujuanPerjalanan.objects.all()
  return HttpResponse(serializers.serialize('json', daftar_perjalanan), content_type="application/json")

def add_perjalanan_json(request):
  if (request.method == 'POST'):
    kota_asal = request.POST.get("kota_asal")
    kota_destinasi = request.POST.get("kota_destinasi")
    
    tujuan_perjalanan = TujuanPerjalanan(
      kota_asal=kota_asal,
      kota_destinasi=kota_destinasi,
    )
    tujuan_perjalanan.save()
    
    return HttpResponse(b"CREATED", status=201)
  
  return HttpResponseNotFound()

@csrf_exempt
def delete_task(request, pk):
  if request.method == "POST":
    item = get_object_or_404(TujuanPerjalanan, id=pk)
    item.delete()
    return JsonResponse({"status": "deleted"})