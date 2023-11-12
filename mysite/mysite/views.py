from django.http import HttpResponse
from django.shortcuts import render
from aplicacion1.models import clases
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("<h1>Hola</h1>")

#@login_required
def Bdatos(request):
    voluntariado= clases.objects.all()
    #voluntariado = clases.objects.filter(tematica= "Juventud" )
    return render(request, 'ver_voluntariado.html' , {"Clases": voluntariado })


 #def buscartematica(request,tematica_elegida):
  #  voluntariado= clases.objects.filter(tematica = tematica_elegida)
   # return render(request, " ",  )