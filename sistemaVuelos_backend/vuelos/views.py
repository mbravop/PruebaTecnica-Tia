from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Vuelo
from .serializers import VueloSerializer

class VueloViewSet(viewsets.ModelViewSet):
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vuelo = serializer.save()

        return Response({
            'vuelo': VueloSerializer(vuelo).data,
            'message': 'Vuelo creado exitosamente'
        }, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = VueloSerializer(data=request.query_params)
        if serializer.is_valid():
            origen = serializer.validated_data['origen']
            destino = serializer.validated_data['destino']
            fecha = serializer.validated_data['fecha']

            queryset = self.get_queryset().filter(origen__iexact=origen, destino__iexact=destino, fecha=fecha)

            if not queryset.exists():
                return Response({"message": "No se encontraron vuelos que coincidan con los criterios."}, status=status.HTTP_404_NOT_FOUND)

            serializer = VueloSerializer(queryset, many=True)
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
