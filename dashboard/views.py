from django.shortcuts import render
from daftar_destinasi.models import Destinasi

def dashboard(request):
  data = Destinasi.objects.all()
  
  context = {
    'data': data,
  }

  return render(request, 'dashboard.html', context)