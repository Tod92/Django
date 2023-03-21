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

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>\
                        <h2>La petite vie de Marie !</h2>')

def listings(request):
    listingsLst = Listing.objects.all()
    liResponse = ''
    for listing in listingsLst:
        liResponse += '<li>' + listing.title + '</li>'
    return HttpResponse(f'<h1>Annonces : </h1> <ul>{liResponse}</ul>')

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1> <p>voici mon 06 08..</p>')
