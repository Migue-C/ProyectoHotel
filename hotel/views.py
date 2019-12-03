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

from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login





def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "hotel/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

from django.contrib.auth.forms import UserCreationForm

# ...

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "hotel/register.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')




























