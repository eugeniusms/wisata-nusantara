from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.core import serializers

from django.contrib.auth.models import User

# Create your views here.
def register(request):
  form = UserCreationForm()

  if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          messages.success(request, 'Akun telah berhasil dibuat!')
          return redirect('authentication:login')
  
  context = {'form':form}
  return render(request, 'register.html', context)

def login_user(request):
  if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user) # melakukan login terlebih dahulu
          response = HttpResponseRedirect(reverse("dashboard:dashboard")) # membuat response
          response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
          return response
      else:
          messages.info(request, 'Username atau Password salah!')
  context = {}
  return render(request, 'login.html', context)

def logout_user(request):
  logout(request)
  response = HttpResponseRedirect(reverse('authentication:login'))
  response.delete_cookie('last_login')
  return response

def show_all_user(request):
  user = User.objects.all()
  return HttpResponse(serializers.serialize("json", user), content_type="application/json")

def show_user_loggedin(request):
  user = User.objects.filter(username=request.user.username)
  return HttpResponse(serializers.serialize("json", user), content_type="application/json")