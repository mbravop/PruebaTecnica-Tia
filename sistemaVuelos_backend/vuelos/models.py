from django.db import models

# Create your models here.

class Vuelo(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    horario = models.TimeField()
    disponibilidad = models.IntegerField()

    class Meta:
        db_table = 'vuelos'

    def __str__(self):
        return f"Vuelo {self.id}: {self.origen} -> {self.destino} ({self.fecha})"