from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import mascota

# Create your views here.

def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html', {'failed' : False})
    elif (request.method == 'POST'):
        return render(request, 'login.html', {'failed' : True})

def carlo(request):
    return render(request, 'carlo.html', {
        'nombre': 'mipene123'
    })

def stats(request):
    carlo = mascota.objects.get(nombre = 'carlo')
    return render(request, 'stats.html', {
        'hambre': carlo.hambre,
        'diversion': carlo.diversion,
        'salud': carlo.salud
    })

def comer(request):
    carlo = mascota.objects.get(nombre = "carlo")
    if (request.method == 'GET'):
        return render(request, 'morfi.html', {'nombre' : carlo.nombre})
    elif (request.method == 'POST'):
        if (carlo.hambre > 0): carlo.hambre -= 10
        carlo.save()
        return redirect('/stats')

def banio(request):
    return render(request, 'banio.html')

# def gym(request):
    # return render(request, 'gym.html')