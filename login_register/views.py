from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

# Create your views here.
def register(request):
  form = UserCreationForm()

  if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          messages.success(request, 'Akun telah berhasil dibuat!')
          return redirect('login_register:login')
  
  context = {'form':form}
  return render(request, 'register.html', context)

def login_user(request):
  if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return redirect('example_app:index')
      else:
          messages.info(request, 'Username atau Password salah!')
  context = {}
  return render(request, 'login.html', context)

def logout_user(request):
  logout(request)
  return redirect('login_register:login')