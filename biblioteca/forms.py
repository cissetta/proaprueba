from django import forms
from .models import Libro, Alumno

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'curso', 'edad']
