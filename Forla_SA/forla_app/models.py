from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
timezone.now()


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=800)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    fechaPublicacion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} - {self.imagen}"


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
