from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import mascota

# Create your views here.

def prueba(request):
    return HttpResponse(request, "¡Bienvenido a Carlito!")

def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html', {'failed' : False})
    elif (request.method == 'POST'):
        return render(request, 'login.html', {'failed' : True})

def carlo(request):
    return render(request, 'carlo.html')

def stats(request):
    return render(request, 'stats.html')

def comer(request):
    if (request.method == 'GET'):
        coso = mascota.objects.get(nombre = "carlo")
        pene = coso.nombre 
        return render(request, 'morfi.html', {'nombre' : pene})
    elif (request.method == 'POST'):
        return render(request, 'morfi.html', {'nombre' : 'default'})

def banio(request):
    return render(request, 'banio.html')

# def gym(request):
    # return render(request, 'gym.html')