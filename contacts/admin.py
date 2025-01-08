from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'phone', 'contact_date') #table columns
    list_display_links = ('id', 'name') # clickable columns to help navigate to the detail page
    search_fields = ('name','listing', 'email', 'phone') #search by
    #take nothe that when a parameter has only one value a comma follows, this is to help ensure your code doesn't run into error 
    list_per_page = 25 #this defines the amount of listings per page (PAGINATION)
    
 
admin.site.register(Contact, ContactAdmin)
