from django.conf.urls import  url
from django.urls import path
from . import views
from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('hotel/acerca/', views.acerca, name='Acercade'),
    path('hotel/contacto/', views.contacto, name='Contacto'),
    path('hotel/inicio/', views.inicio, name='Inicio'),
    path('hotel/agregar_hotel/', views.AgregarHotel, name='AgregarHotel'),   
    path('hotel/modificar_hotel/',views.ModificarHotel, name='ModificarHotel'),
    path('hotel/eliminar_hotel/',views.EliminarHotel, name='EliminarHotel'),
    path('admin/', admin.site.urls), 

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



