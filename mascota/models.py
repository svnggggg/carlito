from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class mascota (models.Model):
    nombre = models.CharField(max_length = 64, null = False)
    salud = models.IntegerField(null = False, default = 100)
    hambre = models.IntegerField(null = False, default = 0)
    diversion = models.IntegerField(null = False, default = 100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.nombre   

class usuario (models.Model):
    nombre = models.CharField(max_length = 64, null = False)
    contrasenia = models.CharField (max_length = 32, null = False)


