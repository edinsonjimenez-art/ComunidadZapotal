from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import (
    Usuario,
    Comunero,
    Categoria,
    Noticia,
    Evento,
    Comentario,
    Reaccion,
    Mensaje,
    Notificacion,
    Multimedia,
    Reporte,
    Autoridad,
    ContactoMensaje,
    LibroReclamacion
)

from .serializers import (
    UsuarioSerializer,
    ComuneroSerializer,
    CategoriaSerializer,
    NoticiaSerializer,
    EventoSerializer,
    ComentarioSerializer,
    ReaccionSerializer,
    MensajeSerializer,
    NotificacionSerializer,
    MultimediaSerializer,
    ReporteSerializer,
    AutoridadSerializer,
    ContactoMensajeSerializer,
    LibroReclamacionSerializer
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ComuneroViewSet(viewsets.ModelViewSet):
    queryset = Comunero.objects.all()
    serializer_class = ComuneroSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class ReaccionViewSet(viewsets.ModelViewSet):
    queryset = Reaccion.objects.all()
    serializer_class = ReaccionSerializer


class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer


class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer


class MultimediaViewSet(viewsets.ModelViewSet):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer


class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer


class AutoridadViewSet(viewsets.ModelViewSet):
    queryset = Autoridad.objects.all()
    serializer_class = AutoridadSerializer


class ContactoMensajeViewSet(viewsets.ModelViewSet):
    queryset = ContactoMensaje.objects.all()
    serializer_class = ContactoMensajeSerializer


class LibroReclamacionViewSet(viewsets.ModelViewSet):
    queryset = LibroReclamacion.objects.all()
    serializer_class = LibroReclamacionSerializer
    permission_classes = [AllowAny]