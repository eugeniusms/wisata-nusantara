from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import serializers
from faq.models import *

# Create your views here.
def show_faq(request):
    return render(request, 'faq.html')

def show_faq_by_json_public(request):
    data = publicFaqData.objects.all()
    print(data)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    

def submit_ajax(request):
    # print('sdasdqwe')
    if request.method == 'POST':
        username = request.POST.get('username')
        question = request.POST.get('question')
        new_question = privateFaqData(user = request.user, username = username, question = question,)
        new_question.save()
    return HttpResponse('')