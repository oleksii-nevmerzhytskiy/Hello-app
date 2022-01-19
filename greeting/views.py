from django.shortcuts import render
from .models import ContactModel
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import *

def greetingView(request):
    return render(request, 'index.html')

def addGreetingView(request):
    x = request.POST['name']
    new_item = ContactModel(name = x)
    if ContactModel.objects.filter(name = new_item.name).exists():
        return render(request, 'index.html',
        {'new_name': 'Вже бачилися, ' + x})
    else:
        new_item.save()
        return render(request, 'index.html',
        {'new_name': 'Привіт, ' + x})

def GreetingListView(request):
    all_greeting_items = ContactModel.objects.all()
    return render(request, 'list.html',
    {'all_items': all_greeting_items})