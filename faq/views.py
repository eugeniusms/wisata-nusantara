import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import serializers
from faq.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

# Create your views here.
def show_faq(request):
    return render(request, 'faq.html')

def show_faq_by_json_public(request):
    data = publicFaqData.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_faq_by_json_private(request):
    data = privateFaqData.objects.filter( user = request.user )
    # print(type(data))
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# @login_required(login_url='/auth/login')
def submit_ajax(request):
    # print('sdasdqwe')
    if request.method == 'POST':
        username = request.POST.get('username')
        question = request.POST.get('question')
        new_question = privateFaqData(user = request.user, username = username, question = question,)
        new_question.save()
    return HttpResponse('')

@csrf_exempt
def add_faq_flutter(request):
    if request.method == "POST":
        faq = json.loads(request.body)
        new_faq = privateFaqData(
            user= request.user,
            username = faq['username'],
            question = faq['question'],
        )
        new_faq.save()
        return JsonResponse({"status" : "success"}, status = 200)

    return JsonResponse({"status" : "failed"}, status = 304)

def get_faq_flutter(request):
    data = privateFaqData.objects.all()
    # print(type(data))
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")