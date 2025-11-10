from django.shortcuts import render
from .models import Alumno, Libro

# Crear las vistas del Sitio.
def index(request):
    print("Index")
    return render(request,'index.html')

def pagina1(request):
    return render(request,'pagina1.html')

def pagina2(request):
    return render(request,'pagina2.html')
