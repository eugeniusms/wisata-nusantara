from django.shortcuts import render

def index(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'index.html', context)