from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('places/', views.places, name='places'),
    path('hotels/', views.hotels, name='hotels'),
    path('hotels/<str:t>', views.hotels, name='hotels'),
    path('hotels/<str:t>/<str:n>', views.hotels, name='hotels'),
    path('place_type/', views.place_type, name='place_type'),
    path('login/', views.login, name='login'),
    path('createaccount/', views.createaccount, name='createaccount'),
    path('planyourtrip/', views.planyourtrip, name='planyourtrip'),
    path('place/', views.place, name='place'),
    path('destination/', views.destination, name='destination'),
    path('destination/<str:d>', views.destination, name='destination'),
    path('holiday_packages', views.holiday_packs, name='holiday_packs'),
    path('packageinfo', views.packageinfo, name='packageinfo'),
    path('buyplan', views.buyplan, name='buyplan'),
    path('user_account/', views.user_account, name='user_account'),
    path('customize', views.customize, name='customize'),
    path('plans', views.plans, name='plans'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
