from django.shortcuts import render
from django.http import HttpResponseRedirect
from cerita_perjalanan.models import ceritaPerjalananItems
from cerita_perjalanan.forms import FormCerita

def submit(request):
    if request.method == 'POST':
        form = FormCerita(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cerita/') # masih gatau ini redirect kemana (?)
    else:
        form = FormCerita()
        
    context = {'form':form}
    return render(request, 'index.html', context)
    
def get(request):
    context = {'cerita':ceritaPerjalananItems.objects.all().filter(user=request.user)} # ini kayaknya bukan cerita doang deh
    return render(request, 'index.html', context)