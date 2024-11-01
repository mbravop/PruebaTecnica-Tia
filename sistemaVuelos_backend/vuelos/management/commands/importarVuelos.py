import csv
from datetime import time, datetime
from itertools import islice
from django.core.management.base import BaseCommand
from vuelos.models import Vuelo
import random as rd

class Command(BaseCommand):
    help = 'Importa datos de vuelos desde un archivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('archivo_csv', type=str, help='Ruta del archivo CSV')

    def handle(self, *args, **kwargs):
        archivo_csv = kwargs['archivo_csv']
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            archivo = csv.DictReader(csvfile)
            contador = 0
            for fila in islice(archivo,300):
                fechaCompleta = datetime.strptime(f"{fila['year']}-{fila['month']}-{fila['day']}", "%Y-%m-%d").date()
                horaString = fila['sched_dep_time']
                horas = int(horaString[:-2])
                minutos = int(horaString[-2:])
                horarioCompleto = time(horas,minutos)
                Vuelo.objects.create(
                    origen=fila['origin'],
                    destino=fila['dest'],
                    fecha=fechaCompleta,
                    horario = horarioCompleto,
                    disponibilidad=str(rd.randint(100,300))
                )
                contador+=1
        self.stdout.write(self.style.SUCCESS('Datos de vuelos importados exitosamente'))
