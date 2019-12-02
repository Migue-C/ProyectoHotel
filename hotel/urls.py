from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('hotel/acerca', views.acerca, name='Acercade'),
    path('hotel/contacto', views.contacto, name='Contacto'),
    path('hotel/inicio', views.inicio, name='Inicio'),
    path('hotel/agregar_hotel', views.AgregarHotel, name='AgregarHotel'),   
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),

    path('admin/', admin.site.urls),        
]


