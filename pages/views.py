from django.shortcuts import render
from django.http import HttpResponse

from realtors.models import Realtor
from listings.models import Listing

from listings.emun import bedroom_choices, price_choices, state_choices


# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Hello World</h1>')

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    data = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
    }
    return render(request, 'pages/index.html', data)

def about(request):
    realtors = Realtor.objects.order_by('-is_mvp', '-hire_date')
    mvp_realtor = Realtor.objects.filter(is_mvp=True)
    data = {'realtors' : realtors, 'mvp_realtor': mvp_realtor}
    return render(request, 'pages/about.html', data)