from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Reserva
        fields = ('id', 'usuario', 'vuelo', 'estado')
        read_only_fields = ('id', 'usuario', 'estado')
