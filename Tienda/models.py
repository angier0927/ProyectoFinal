from django.db import models

class Articulo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_producto = models.CharField(max_length = 60)
    precio = models.IntegerField(blank=True, null=True)
    categoria = models.CharField(max_length=50)
    disponibilidad = models.CharField(max_length= 10)
    descuento = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre_producto

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_usuario = models.CharField(max_length = 60)
    identificacion = models.CharField(max_length = 60)
    telefono = models.CharField(max_length = 60)
    medio_pago = models.CharField(max_length = 60)
    entrega = models.CharField(max_length = 60)
    direccion = models.CharField(max_length = 60)

    def __str__(self):
        return self.nombre_usuario


