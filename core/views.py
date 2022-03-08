from django.http import HttpResponse
from django.shortcuts import render
from .models import Place

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


def place_type(request):
    return render(request, 'place_type.html')


def login(request):
    return render(request, 'loginpage.html')

def createaccount(request):
    return render(request, 'createaccount.html')

def planyourtrip(request):
    return render(request, 'planyourtrip.html')


def place(request):
    q = request.GET.get('q')
    type =  request.GET.get('type')
    if request.method == 'GET':
        if not type:      
            data = Place.objects.filter(city=q).order_by('id')[:8]
            context = {'place': q,'data': data}
            return render(request, 'place.html', context)
        elif type and q:
            data = Place.objects.filter(city=q, tag=type)
            context = {'place': q,'data': data}
            return render(request, 'place.html', context)
