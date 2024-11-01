from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Reserva
from .serializers import ReservaSerializer
from vuelos.models import Vuelo

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        vuelo = Vuelo.objects.get(id=data['vuelo'])
        
        try:
            vuelo = Vuelo.objects.get(id=data['vuelo'])
        except Vuelo.DoesNotExist:
            return Response({"detail": "Vuelo no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        if vuelo.disponibilidad <= 0:
            return Response(
                {"detail": "No hay disponibilidad para este vuelo."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if Reserva.objects.filter(usuario=request.user, vuelo=vuelo).exists():
            return Response(
            {"detail": "Ya tienes una reserva para este vuelo."},
            status=status.HTTP_400_BAD_REQUEST
        )
        vuelo.disponibilidad -= 1
        vuelo.save()
        
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(usuario=request.user)
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request,usuarioId=None, *args, **kwargs):
        queryset = self.queryset.filter(usuario=usuarioId)
        serializer = self.get_serializer(queryset, many=True)
        
        if not queryset.exists():
                return Response({"message": "No se encontraron reservas para el usuario "+str(usuarioId)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
    
    def cancelar(self, request, pk=None):
        try:
            reserva = self.queryset.get(pk=pk)
            if reserva.usuario != request.user:
                return Response(
                    {"detail": "No tienes permiso para cancelar esta reserva."},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            if not reserva.estado:
                return Response(
                    {"detail": "Esta reserva ya está cancelada."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            reserva.estado = False
            reserva.save()
            vuelo = Vuelo.objects.get(id=reserva.vuelo.id)
            vuelo.disponibilidad += 1
            vuelo.save()
            return Response({"detail": "Reserva cancelada exitosamente."}, status=status.HTTP_200_OK)
        except Reserva.DoesNotExist:
            return Response({"detail": "Reserva no encontrada."}, status=status.HTTP_404_NOT_FOUND)
