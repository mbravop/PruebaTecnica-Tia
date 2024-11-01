# vuelos/serializers.py
from rest_framework import serializers
from .models import Vuelo

class VueloSerializer(serializers.ModelSerializer):
    origen = serializers.CharField(required=True)
    destino = serializers.CharField(required=True)
    fecha = serializers.DateField(required=True) 
    
    class Meta:
        model = Vuelo
        fields = '__all__'
        extra_kwargs = {
            'horario': {'required': False},
            'disponibilidad': {'required': False},
        }
