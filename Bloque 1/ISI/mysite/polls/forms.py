from django import forms
from .models import *


class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Peliculas
        fields = [
            'nombre',
            'fecha_de_estreno',
            'precio_alquiler',
            'director',
            'videoclub_dato',
        ]

        labels = {
            'nombre':'Título',
            'videoclub_dato':'Videoclub',
            'fecha_de_estreno':'Fecha',
            'precio_alquiler':'Precio Alquiler',
            'director':'Director',
            
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_de_estreno':forms.DateInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_alquiler': forms.TextInput(attrs={'class': 'form-control'}),
            'videoclub_dato': forms.TextInput(attrs={'class': 'form-control'}),
         #'precio alquiler': forms.FloatField(),
            # 'caratula': forms.ImageField(),
            # 'imagen_promocional': forms.ImageField(),
        }

class SociosForm(forms.ModelForm):

    class Meta:
        model = Socios
        fields = [
            'nombre',
            'edad',
            'email',
            'sexo',
          
        ]

        labels = {
            'nombre':'Nombre',
            'edad':'Edad',
            'email':'Correo Electronico',
            'sexo':'Sexo',
            
            
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
           
         #'precio alquiler': forms.FloatField(),
            # 'caratula': forms.ImageField(),
            # 'imagen_promocional': forms.ImageField(),
        }


class AlquileresForm(forms.ModelForm):

    class Meta:
        model = Alquileres
        Alquileres.total_a_pagar =  Peliculas.precio_alquiler 
        fields = [
            'fecha_de_recogida',
            'fecha_de_devolucion',
            'nombre',
            'total_a_pagar',
        ]

        labels = {
            
            'fecha_de_recogida':'Fecha de recogida',
            'fecha_de_devolucion':'Fecha de devolucion',
            'nombre':'Nombre',
            'total_a_pagar' : 'Total',
        }
        widgets = {
            
            'fecha_de_recogida': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_de_devolucion': forms.DateInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'total_a_pagar' : forms.NumberInput(attrs={'class': 'form-control','value':Peliculas.precio_alquiler })
         #'precio alquiler': forms.FloatField(),
            # 'caratula': forms.ImageField(),
            # 'imagen_promocional': forms.ImageField(),
        }

class EstadisticasForm(forms.ModelForm):

    class Meta:
        model = Estadisticas
        fields = [
            
            'fecha_de_creacion',
            
        ]

        labels = {
            
            'fecha_de_creacion':'Fecha de creación',
            
        }
        widgets = {
            
            'fecha_de_creacion': forms.SelectDateWidget(),
            
  
         #'precio alquiler': forms.FloatField(),
            # 'caratula': forms.ImageField(),
            # 'imagen_promocional': forms.ImageField(),
        }