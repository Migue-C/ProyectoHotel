from django.conf.urls import  url
from django.urls import path
from . import views
from django.contrib import admin 


urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('hotel/acerca', views.acerca, name='Acercade'),
    path('hotel/contacto', views.contacto, name='Contacto'),
    path('hotel/inicio', views.inicio, name='Inicio'),
    path('hotel/agregar_hotel', views.AgregarHotel, name='AgregarHotel'),   
    path('admin/', admin.site.urls),  

]