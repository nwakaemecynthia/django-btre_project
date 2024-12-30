from django.shortcuts import render
from django.http import HttpResponse

from realtors.models import Realtor
from listings.models import Listing


# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Hello World</h1>')

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    return render(request, 'pages/index.html', {'listings': listings})

def about(request):
    realtors = Realtor.objects.order_by('-is_mvp', '-hire_date')
    mvp_realtor = Realtor.objects.filter(is_mvp=True)
    context = {'realtors' : realtors, 'mvp_realtor': mvp_realtor}
    return render(request, 'pages/about.html', context)

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')