import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from cerita_perjalanan.models import ceritaPerjalananItems
from cerita_perjalanan.forms import FormCerita
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@csrf_exempt
@login_required(login_url='/auth/login')
def submit_cerita(request):
    if request.method == 'POST':
        form = FormCerita(request.POST)
        form.instance.name = request.user.username
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/story/')
    else:
        form = FormCerita()
    
    context = {
        'form':form,
        'cerita':ceritaPerjalananItems.objects.all(),
        'username':request.user.username
        }
    return render(request, 'cerita-perjalanan.html', context)

@csrf_exempt
def submit_cerita_json(request):
    if request.method == 'POST':
        res = json.loads(request.body)
        review = res['review']
        name = res['username']
        story = ceritaPerjalananItems(
            name = name,
            review = review,
        )
        story.save()
        return JsonResponse({"status" : "success"}, status = 200)
    return JsonResponse({"status" : "failed"}, status = 304)

def get_cerita(request):
    form = FormCerita()
    username = request.user.username
    context = {
        'cerita':ceritaPerjalananItems.objects.all(),
        'username':username,
        'form':form
    }
    
    return render(request, 'cerita-perjalanan.html', context)

def get_cerita_json(request):
    story = ceritaPerjalananItems.objects.all()
    return HttpResponse(
        serializers.serialize(
            "json", 
            story),
        content_type="application/json")
    
@csrf_exempt
@login_required(login_url='/auth/login')
def delete_cerita_json(request, id):
    task = ceritaPerjalananItems.objects.get(pk=id)
    task.delete()
    return JsonResponse({"object": "Data dihapus"},status=200)
        
@csrf_exempt
@login_required(login_url='/auth/login')
def delete_cerita(request, id):
    task = ceritaPerjalananItems.objects.get(pk=id)
    task.delete()
    return HttpResponseRedirect("/story/")
        
