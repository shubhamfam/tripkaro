from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('places/', views.places, name='places'),
    path('hotels/', views.hotels, name='hotels'),
    path('place_type/', views.place_type, name='place_type'),
    path('login/', views.login, name='login'),
    path('createaccount/', views.createaccount, name='createaccount'),
    path('planyourtrip/', views.planyourtrip, name='planyourtrip'),
    path('place/', views.place, name='place'),
]