from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde django")

def miEdad(request, edad):
    return HttpResponse("Hola tu edad es: %s" %edad)

def index(request):
    return render(request, 'index.html')


def alumno(request):
    return render(request, 'alumnos.html')

def buscar(request):
    return render(request, 'busqueda_alumnos.html')

def materia(request):
    return render(request, 'materia.html')

def buscarM(request):
    return render(request, 'busqueda_materia.html')