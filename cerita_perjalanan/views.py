from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ceritaPerjalananItem
from .forms import FormCerita
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from cerita_perjalanan.forms import taskform
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound

def get_review(request):
    review = ceritaPerjalananItem.objects.all()
    context = {
        'cerita':get_review,
    }
    response = {'get_review':get_review}
    return render(request, 'review.html', context, response)

def submit_review(request):
    form = FormCerita()
    if request.method == 'POST':
        form = FormCerita(request.POST)
        if form.is_valid():
             review = ceritaPerjalananItem()
             review.name = form.cleaned_data['name']
            #  review.email = form.cleaned_data['email']
             review.review = form.cleaned_data['review']
             form.save()
             return HttpResponseRedirect(reverse('cerita_perjalanan: submit_review'))
        
    context = {'form':form}
    return render(request, 'index.html', context)