from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola a todos, esta es mi primera aplicacion en Django")