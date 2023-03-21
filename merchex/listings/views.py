from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>\
                        <h2>La petite vie de Marie !</h2>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>ici une liste</p>')

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1> <p>voici mon 06 08..</p>')
