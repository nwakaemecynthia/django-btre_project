from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

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
    return render(request, 'listings/search.html')