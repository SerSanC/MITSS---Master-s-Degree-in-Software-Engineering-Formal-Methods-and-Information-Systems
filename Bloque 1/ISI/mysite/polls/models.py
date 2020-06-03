import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Videoclub(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    nombre_gerente = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=5)
    def _str_(self):
        return self.nombre

class Peliculas(models.Model):
    id = models.AutoField(primary_key=True)
    videoclub_dato = models.CharField(max_length=25,default="", editable=True)
    nombre = models.CharField(max_length=25)
    director = models.CharField(max_length=25)
    fecha_de_estreno = models.DateField(max_length = 25)
    precio_alquiler = models.FloatField(max_length=25)
    key = models.ForeignKey(Videoclub, on_delete = models.CASCADE,default="", editable=False)
    def _str_(self):
        return self.nombre        

class Socios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=25,default="", editable=True)
    email = models.CharField(max_length=25,default="", editable=True)
    #videoclub = models.CharField(max_length=25,default="", editable=True)
    def _str_(self):
        return self.nombre   

class Alquileres(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_de_recogida = models.DateField(max_length = 25)
    fecha_de_devolucion = models.DateField(max_length = 25)
    nombre = models.CharField(max_length=25,default="", editable=True)
    total_a_pagar = models.FloatField()
    def _str_(self):
        return self.nombre   

class Estadisticas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_de_creacion = models.DateField(max_length = 25)
    total_gastado = models.FloatField()
    def _str_(self):
        return self.nombre   

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    def _str_(self):
        return self.nombre   