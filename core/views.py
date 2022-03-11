from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Hotel


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contactus.html')


def places(request):
    return render(request, 'places.html')


def hotels(request, t=None, n=None):
    if t == None and n == None:
        return render(request, 'hotels.html')
    elif t and not n:
        hotels = Hotel.objects.filter(type=t)[:9]
        context = {'hotels': hotels}
        return render(request, 'hotels.html', context)
    elif n:
        h = Hotel.objects.filter(name=n)[0]
        context = {'h': h}
        return render(request, 'hotels.html', context)

def place_type(request):
    return render(request, 'place_type.html')


def login(request):
    return render(request, 'loginpage.html')


def createaccount(request):
    return render(request, 'createaccount.html')


def planyourtrip(request):
    return render(request, 'planyourtrip.html')


def place(request):
    q = (request.GET.get('q')).capitalize()
    type = request.GET.get('type')
    if request.method == 'GET':
        if not type:
            destinations = Place.objects.filter(city=q).order_by('id')[:8]
            hotels = Hotel.objects.filter(city=q, star_rating__gt=3)[:8]
            context = {
                'place': q,
                'destinations': destinations,
                'hotels': hotels
            }
            return render(request, 'place.html', context)
        elif type and q:
            destinations = Place.objects.filter(city=q, tag=type)[:8]
            context = {'place': q, 'destinations': destinations, 'type': type}
            return render(request, 'place.html', context)


def destination(request, d=None):
    dest = Place.objects.filter(name=d)[0]
    context = {'destination': dest}
    return render(request, 'destination.html', context)


def holiday_packs(request):
    return render(request, 'holiday_packages.html')


def packageinfo(request):
    return render(request, 'packageinfo.html')


def buyplan(request):
    return render(request, 'buyplan.html')

def user_account(request):
    return render(request, 'user_account.html')

def customize(request):
    return render(request, 'customize.html')

def plans(request):
    city = request.GET.get('city')
    dest = request.GET.get('destination')
    min = int(request.GET.get('budget-min'))
    max = int(request.GET.get('budget-max'))
    budget = (min+ max) //2
    context = {'city': city, 'destination': dest, 'budget': budget}
    return render(request, 'plans.html', context)
