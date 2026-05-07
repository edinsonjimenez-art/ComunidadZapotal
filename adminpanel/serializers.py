from rest_framework import serializers
from .models import (
    Usuario, Comunero, Categoria, Noticia, Evento,
    Comentario, Reaccion, Mensaje, Notificacion,
    Multimedia, Reporte
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class ComuneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunero
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

from rest_framework import serializers
from .models import Evento, Multimedia


class MultimediaSerializer(serializers.ModelSerializer):
    archivo_url = serializers.SerializerMethodField()

    class Meta:
        model = Multimedia
        fields = ["id", "archivo_url", "tipo", "orden"]

    def get_archivo_url(self, obj):
        request = self.context.get("request")
        if obj.archivo and request:
            return request.build_absolute_uri(obj.archivo.url)
        return None


class EventoSerializer(serializers.ModelSerializer):
    multimedia = MultimediaSerializer(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = [
            "id",
            "titulo",
            "descripcion",
            "fecha_evento",
            "estado",
            "categoria",
            "usuario",
            "multimedia",
        ]
        

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'


# SERIALIZER DE REACCIONES

class ReaccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reaccion
        fields = [
            "id",
            "tipo",
            "usuario",
            "noticia",
            "evento",
        ]

    def validate(self, data):

        noticia = data.get("noticia")
        evento = data.get("evento")

        # SOLO UNO
        if noticia and evento:
            raise serializers.ValidationError(
                "No puedes reaccionar a noticia y evento al mismo tiempo."
            )

        if not noticia and not evento:
            raise serializers.ValidationError(
                "Debes seleccionar una noticia o un evento."
            )

        return data


class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'


class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'


class MultimediaSerializer(serializers.ModelSerializer):
    archivo_url = serializers.SerializerMethodField()

    class Meta:
        model = Multimedia
        fields = ["id", "archivo_url", "tipo", "orden"]

    def get_archivo_url(self, obj):
        request = self.context.get("request")
        if obj.archivo and request:
            return request.build_absolute_uri(obj.archivo.url)
        return None


class NoticiaSerializer(serializers.ModelSerializer):
    multimedia = MultimediaSerializer(many=True, read_only=True)

    class Meta:
        model = Noticia
        fields = [
            "id",
            "titulo",
            "contenido",
            "fecha_publicacion",
            "estado",
            "categoria",
            "usuario",
            "multimedia",
        ]


class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'