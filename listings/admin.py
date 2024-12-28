from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') #table columns
    list_display_links = ('id', 'title') # clickable columns to help navigate to the detail page
    list_filter = ('realtor',) #aside filter (this is not the table header filter as the heder filter is default for all table header)
    list_editable = ('is_published',) #allows you mutate data from the table afterwards you have to save to effectively update your changes
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') #search by
    #take nothe that when a parameter has only one value a comma follows, this is to help ensure your code doesn't run into error 
    list_per_page = 25 #this defines the amount of listings per page (PAGINATION)
    
 
admin.site.register(Listing, ListingAdmin)