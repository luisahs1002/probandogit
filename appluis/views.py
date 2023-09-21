from django.shortcuts import render
from django.http import HttpResponse
from appluis.models import *
# Create your views here.

def curso(request):

    curso1 = Curso(nombre = "JOSEMAR", camada = "9452")
    curso1.save()
    return HttpResponse(F"HOLA {curso1.nombre} TU CAMADA ESTE AÑO ES: {curso1.camada},ESPERAMOS QUE TE VAYA BIEN ESTE AÑO")

def inicio(request):
    return render( request ,"appluis/inicio.html")


def estudiante(request):
    estudiante1 = Estudiante(nombre="LUIS",apellido="HERNANDEZ",correo="luisalejandro.lahs@gmail.com")
    estudiante1.save()
    return render(request, "appluis/estudiante.html") 

def entregable(request):
    return HttpResponse("ESTA ES LA PANTALLA DEL ENTREGALE")

