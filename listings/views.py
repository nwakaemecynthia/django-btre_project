from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing
from .emun import bedroom_choices, price_choices, state_choices


# Create your views here.

def index(request):
    # return render(request, 'listings/listings.html', {
    #     'name': 'Brad'
    # })
    
    # listings = Listing.objects.all() #Fetch all data from DB
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)  #Paginate the data where 6 is the page size (total number of data per page)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/listings.html', {'listings': paged_listings})


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/listing.html', {'listing': listing})

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
            
    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) #`__iexact` allows for case insensitivity but `__exact` is case sensitive
    
    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state) 
            
    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)#when a search is 4; lte implies: get all beaddrooms from 4 below (Less Than Equalto) 
    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    
    data = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', data)