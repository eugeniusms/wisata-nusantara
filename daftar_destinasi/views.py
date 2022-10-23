from django.shortcuts import render

# Create your views here.
def daftar_destinasi(request):
  return render(request, 'daftar-destinasi.html')