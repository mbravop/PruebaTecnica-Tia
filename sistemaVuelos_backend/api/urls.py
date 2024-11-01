from django.urls import path, include

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('vuelos/', include('vuelos.urls')),
    path('reservas/', include('reservas.urls')),
]
