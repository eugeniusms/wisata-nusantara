from django.shortcuts import render
from django.http import HttpResponseRedirect
from cerita_perjalanan.models import ceritaPerjalananItem
from cerita_perjalanan.forms import FormCerita

def submit(request):
    if request.method == 'POST':
        username = request.user.username
        form = FormCerita(request.POST, username = username)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cerita')
    else:
        form = FormCerita()
    
    context = {
        'form':form,
        'cerita':ceritaPerjalananItem.objects.all(),
        'username':request.user.username
        }
    return render(request, 'cerita_perjalanan.html', context)

def get(request):
    form = FormCerita()
    username = request.user.username
    context = {
        'cerita':ceritaPerjalananItem.objects.all(),
        'username':username,
        'form':form
    }
    print(request.user.username)
    
    return render(request, 'cerita_perjalanan.html', context)