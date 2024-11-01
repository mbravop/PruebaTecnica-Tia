from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, LoginView
from reservas.views import ReservaViewSet

router = DefaultRouter()
router.register(r'', UsuarioViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
    path('<int:usuarioId>/reservas/', ReservaViewSet.as_view({'get': 'list'}), name='listar_reservas_usuario'),
]