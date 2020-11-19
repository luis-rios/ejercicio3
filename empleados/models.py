from django.db import models

from administradores.models import Administrador
from areas.models import Area


class Empleado(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField(default=True)
    job = models.CharField(max_length=200)

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    administrador = models.ManyToManyField(Administrador, related_name='admnistrador')

    def __str__(self):
        return self.name
