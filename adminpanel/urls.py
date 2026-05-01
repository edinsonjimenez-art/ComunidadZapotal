from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, ComuneroViewSet, CategoriaViewSet,
    NoticiaViewSet,
    EventoViewSet, ComentarioViewSet, ReaccionViewSet,
    MensajeViewSet, NotificacionViewSet, MultimediaViewSet,
    ReporteViewSet
)

router = DefaultRouter()

router.register('usuarios', UsuarioViewSet)
router.register('comuneros', ComuneroViewSet)
router.register('categorias', CategoriaViewSet)
router.register('noticias', NoticiaViewSet)
router.register('eventos', EventoViewSet)
router.register('comentarios', ComentarioViewSet)
router.register('reacciones', ReaccionViewSet)
router.register('mensajes', MensajeViewSet)
router.register('notificaciones', NotificacionViewSet)
router.register('multimedia', MultimediaViewSet)
router.register('reportes', ReporteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]