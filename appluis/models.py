from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
