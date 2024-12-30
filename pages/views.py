from django.shortcuts import render
from django.http import HttpResponse

from realtors.models import Realtor


# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Hello World</h1>')

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    realtors = Realtor.objects.all
    context = {'realtors' : realtors}
    return render(request, 'pages/about.html', context)

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')