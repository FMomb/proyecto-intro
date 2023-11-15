from django.shortcuts import render
from django.http import HttpRequest
from models import clases
from forms import formulario
# Create your views here.
class formularioview(HttpRequest):
    
    def index(request):
        clase = formulario()
        return render(request, "voluntariadoIndex.html",{"form": clase})
    
    def procesarformulario(request):
        clase = formulario() 
        if clase.is_valid(): 
            clase.save()
            clase= formulario