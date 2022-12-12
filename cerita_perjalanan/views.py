from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from cerita_perjalanan.models import ceritaPerjalananItems
from cerita_perjalanan.forms import FormCerita
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
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
@login_required(login_url='/auth/login')
def submit_cerita_json(request):
    if request.method == 'POST':
        cerita = json.loads(request.body)
        
        review = cerita['review']
        user_id = cerita['id']
        name = User.objects.get(id=user_id)
        story = ceritaPerjalananItems.objects.create(
            name = name.get_full_name(),
            review = review,
            )
    return JsonResponse([story,], safe=False, status=200) 


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
        
