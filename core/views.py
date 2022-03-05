from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contactus.html')

def places(request):
    return render(request, 'places.html')

def hotels(request):
    return render(request, 'hotels.html')