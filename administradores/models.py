from django.db import models


class Administrador(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
