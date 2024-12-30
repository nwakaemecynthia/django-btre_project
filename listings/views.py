from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

# Create your views here.

def index(request):
    # return render(request, 'listings/listings.html', {
    #     'name': 'Brad'
    # })
    listings = Listing.objects.all()
    #Paginate the data where 3 is the page size (total number of data per page)
    paginator = Paginator(listings, 3)  # Show 25 contacts per page.
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)


    
    context = {'listings' : paged_listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')