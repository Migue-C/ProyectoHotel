from django.shortcuts import render
from django.utils import timezone
from .models import Hotel
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.contrib.auth.models import User

# Create your views here.

def hotel_list(request):
    hoteles = Hotel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'hotel/hotel_list.html', {'hoteles': hoteles})    

def acerca(request):
    return render(request, 'hotel/Acercade.html')

def contacto(request):
    return render(request, 'hotel/Contacto.html')

def inicio(request):
    return render(request, 'hotel/Inicio.html')

def AgregarHotel(request):
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = PostForm(request.POST)
        if form.is_valid():
            Hotel = form.save(commit=False)
            Hotel.title = request.POST['title']
            Hotel.text = request.POST['text']
            Hotel.author = request.user
            Hotel.published_date = timezone.now()
 
            Hotel.save()
    else:
        form = PostForm()   
    return render(request, "hotel/agregar_hotel.html", {'form': form})






















