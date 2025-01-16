from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

from decouple import config
from .models import Contact


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        listing = request.POST['listing']
        user_id = request.POST['user_id']
        listing_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        
        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contact = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contact:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)
        else:
            has_contact = Contact.objects.all().filter(listing_id=listing_id, email=email)
            if has_contact:
                messages.error(request, 'You have already made an inquiry for this listing with this email address')
                return redirect('/listings/'+listing_id)
       

        contact = Contact(listing=listing, user_id=user_id, listing_id=listing_id, name=name, email=email, phone=phone, message=message)
        
        contact.save()
        
        # Send Email after saving listing inquiry 
        send_mail(
            f'Property Listing Inquiry - {listing}',  # SUBJECT
            f"There has been an inquiry for {listing}. Sign into the admin panel for more information.",  # BODY
            config('EMAIL_HOST_USER', default='cynthia@example.co'), # FROM
            [realtor_email, config('EMAIL_HOST_USER', default='cynthia@example.co')],  # TO
            fail_silently=False # FAIL SILENTLY
        )
                    
        messages.success(request, 'Your request has been submitted, A realtor will get back to you soon.')
        return redirect('/listings/'+listing_id)