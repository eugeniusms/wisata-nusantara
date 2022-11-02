from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from cerita_perjalanan.models import ceritaPerjalananItems
from cerita_perjalanan.forms import FormCerita
from django.core import serializers

def submit(request):
    if request.method == 'POST':
        username = request.user.username
        form = FormCerita(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/review/')
    else:
        form = FormCerita()
    
    context = {
        'form':form,
        'cerita':ceritaPerjalananItems.objects.all(),
        'username':request.user.username
        }
    return render(request, 'cerita-perjalanan.html', context)

def get(request):
    form = FormCerita()
    username = request.user.username
    context = {
        'cerita':ceritaPerjalananItems.objects.all(),
        'username':username,
        'form':form
    }
    # print(ceritaPerjalananItems.objects.all())
    
    return render(request, 'cerita-perjalanan.html', context)

def submit(request):
    if request.method == "POST":
        form = FormCerita(request.POST)
        form.instance.name = request.user.username
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect("/review/")
            return response
    else:
        form = FormCerita()

    context = {'form':form}
    return render(request, 'cerita-perjalanan.html', context)