from django.contrib import admin
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
)

admin.site.register(Usuario)
admin.site.register(Comunero)
admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Evento)
admin.site.register(Comentario)
admin.site.register(Reaccion)
admin.site.register(Mensaje)
admin.site.register(Notificacion)
admin.site.register(Multimedia)
admin.site.register(Reporte)