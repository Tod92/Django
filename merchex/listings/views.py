from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/hello.html',
                  {'first_band': bands[0],
                   'bands': bands})
def contact(request):
    return render(request,
                  'listings/contact.html')

def about(request):
    return render(request,
                  'listings/about.html')

def listings(request):
    listingsLst = Listing.objects.all()

    return render(request,
                  'listings/listings.html',
                  {'listings' : listingsLst})

