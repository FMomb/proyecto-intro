from django.http import HttpResponse
from django.shortcuts import render
from aplicacion1.models import clases


def index(request):
    return HttpResponse("<h1>Hola</h1>")
def Bdatos(request):
    voluntariado= clases.objects.all()
    return render(request, 'ver_voluntariado.html' , {"Clases": voluntariado })