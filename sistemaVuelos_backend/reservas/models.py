from django.db import models
from django.conf import settings

class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vuelo = models.ForeignKey('vuelos.Vuelo', on_delete=models.CASCADE) 
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'reservas'

    def __str__(self):
        return f'Reserva {self.id} - Usuario: {self.usuario.email}, Vuelo: {self.vuelo}'
