from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Grupo 15</h1> <h1>Integrantes:<h1> "
                         "<h3>Maximiliano Martínez<h3>""<h3>")
