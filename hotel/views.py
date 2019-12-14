from django.shortcuts import render
from django.utils import timezone
from .models import Hotel
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def hotel_list(request):
    hoteles = Hotel.objects.all()
    data={
        'hoteles':hoteles
    }
    
    return render(request, 'hotel/hotel_list.html', data)    

def acerca(request):
    return render(request, 'hotel/Acercade.html')

def contacto(request):
    return render(request, 'hotel/Contacto.html')

def inicio(request):
    return render(request, 'hotel/Inicio.html')



@permission_required('hotel.addhotel')
def AgregarHotel(request):
    data = {
        'form':PostForm()
    }
    
    if request.method == 'POST':
        formulario= PostForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data ['mensaje'] = "El Hotel Fue Guardado Correctamente"

    return render(request, "hotel/agregar_hotel.html", data)



@permission_required('hotel.changehotel')


def ModificarHotel(request):
    data = {
        'form' : PostForm()
    }
    if request.method == 'POST':
        formulario= PostForm(data=request.POST, instance=hoteles)
        if formulario.is_valid():
            formulario.save()
            data ['mensaje'] = "El Hotel Fue Modificado Correctamente"
            data['form'] = formulario


    return render(request, "hotel/modificar_hotel.html", data)






















