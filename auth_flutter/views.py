import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Successfully Logged In!"
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)

        username = data["username"]
        password1 = data["password1"]
        password2 = data["password2"]

        if password1 != password2:
            return JsonResponse({'status': 'failed', 'message': 'Gagal woi'})

        new_user = User.objects.create_user(username = username, password = password1)
        new_user.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
  
@csrf_exempt
def logout(request):
    try:
        logout(request)
        return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged out!",
                }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)