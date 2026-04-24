
from django.db import models
from django.core.exceptions import ValidationError


class Usuario(models.Model):
    class TipoUsuario(models.TextChoices):
        ADMIN = 'ADMIN', 'ADMIN'
        COMUNERO = 'COMUNERO', 'COMUNERO'
        USUARIO = 'USUARIO', 'USUARIO'

    class EstadoUsuario(models.TextChoices):
        ACTIVO = 'ACTIVO', 'ACTIVO'
        INACTIVO = 'INACTIVO', 'INACTIVO'

    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    password = models.CharField(max_length=255, verbose_name="Contraseña")
    dni = models.CharField(max_length=8, verbose_name="DNI")
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TipoUsuario.choices,
        verbose_name="Tipo de usuario"
    )
    estado = models.CharField(
        max_length=10,
        choices=EstadoUsuario.choices,
        default=EstadoUsuario.ACTIVO,
        verbose_name="Estado"
    )
    dni_verificado = models.BooleanField(default=False, verbose_name="DNI verificado")
    foto_perfil = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Foto de perfil"
    )
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    class Meta:
        db_table = 'usuario'
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    def clean(self):
        if self.dni and len(self.dni) != 8:
            raise ValidationError("El DNI debe tener exactamente 8 dígitos.")


class Comunero(models.Model):
    class EstadoComunero(models.TextChoices):
        ACTIVO = 'ACTIVO', 'ACTIVO'
        INACTIVO = 'INACTIVO', 'INACTIVO'

    dni = models.CharField(max_length=8, unique=True, verbose_name="DNI oficial")
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    estado = models.CharField(
        max_length=10,
        choices=EstadoComunero.choices,
        default=EstadoComunero.ACTIVO,
        verbose_name="Estado"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='comuneros',
        verbose_name="Usuario asociado"
    )

    class Meta:
        db_table = 'comunero'
        verbose_name = "Comunero"
        verbose_name_plural = "Comuneros"
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    def clean(self):
        if self.dni and len(self.dni) != 8:
            raise ValidationError("El DNI del comunero debe tener exactamente 8 dígitos.")


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        db_table = 'categoria'
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    class EstadoNoticia(models.TextChoices):
        ACTIVO = 'ACTIVO', 'ACTIVO'
        INACTIVO = 'INACTIVO', 'INACTIVO'

    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='noticias',
        verbose_name="Categoría"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='noticias',
        verbose_name="Usuario responsable"
    )
    fecha_publicacion = models.DateTimeField(verbose_name="Fecha de publicación")
    estado = models.CharField(
        max_length=10,
        choices=EstadoNoticia.choices,
        default=EstadoNoticia.ACTIVO,
        verbose_name="Estado"
    )

    class Meta:
        db_table = 'noticia'
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo

    def clean(self):
        if self.usuario and self.usuario.tipo_usuario != Usuario.TipoUsuario.ADMIN:
            raise ValidationError("Solo un usuario ADMIN puede publicar noticias.")


class Evento(models.Model):
    class EstadoEvento(models.TextChoices):
        ACTIVO = 'ACTIVO', 'ACTIVO'
        INACTIVO = 'INACTIVO', 'INACTIVO'

    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='eventos',
        verbose_name="Categoría"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='eventos',
        verbose_name="Usuario responsable"
    )
    fecha_evento = models.DateTimeField(verbose_name="Fecha del evento")
    fecha_publicacion = models.DateTimeField(verbose_name="Fecha de publicación")
    estado = models.CharField(
        max_length=10,
        choices=EstadoEvento.choices,
        default=EstadoEvento.ACTIVO,
        verbose_name="Estado"
    )

    class Meta:
        db_table = 'evento'
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-fecha_evento']

    def __str__(self):
        return self.titulo

    def clean(self):
        if self.usuario and self.usuario.tipo_usuario != Usuario.TipoUsuario.ADMIN:
            raise ValidationError("Solo un usuario ADMIN puede publicar eventos.")


class Comentario(models.Model):
    class EstadoComentario(models.TextChoices):
        APROBADO = 'APROBADO', 'APROBADO'
        PENDIENTE = 'PENDIENTE', 'PENDIENTE'
        RECHAZADO = 'RECHAZADO', 'RECHAZADO'

    contenido = models.TextField(verbose_name="Contenido")
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='comentarios',
        verbose_name="Usuario"
    )
    noticia = models.ForeignKey(
        Noticia,
        on_delete=models.CASCADE,
        related_name='comentarios',
        null=True,
        blank=True,
        verbose_name="Noticia"
    )
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='comentarios',
        null=True,
        blank=True,
        verbose_name="Evento"
    )
    comentario_padre = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='respuestas',
        null=True,
        blank=True,
        verbose_name="Comentario padre"
    )
    estado = models.CharField(
        max_length=10,
        choices=EstadoComentario.choices,
        default=EstadoComentario.PENDIENTE,
        verbose_name="Estado"
    )
    tiene_palabras_prohibidas = models.BooleanField(
        default=False,
        verbose_name="Tiene palabras prohibidas"
    )
    editado = models.BooleanField(default=False, verbose_name="Editado")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    class Meta:
        db_table = 'comentario'
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-fecha']

    def __str__(self):
        return f"Comentario #{self.id} - {self.usuario}"

    def clean(self):
        if self.noticia and self.evento:
            raise ValidationError("Un comentario no puede estar asociado a noticia y evento al mismo tiempo.")
        if not self.noticia and not self.evento:
            raise ValidationError("Un comentario debe estar asociado a una noticia o a un evento.")
        if self.comentario_padre:
            if self.noticia and self.comentario_padre.noticia != self.noticia:
                raise ValidationError("El comentario padre debe pertenecer a la misma noticia.")
            if self.evento and self.comentario_padre.evento != self.evento:
                raise ValidationError("El comentario padre debe pertenecer al mismo evento.")


class Reaccion(models.Model):
    class TipoReaccion(models.TextChoices):
        LIKE = 'LIKE', 'LIKE'
        LOVE = 'LOVE', 'LOVE'
        ENOJO = 'ENOJO', 'ENOJO'

    tipo = models.CharField(
        max_length=10,
        choices=TipoReaccion.choices,
        verbose_name="Tipo"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='reacciones',
        verbose_name="Usuario"
    )
    noticia = models.ForeignKey(
        Noticia,
        on_delete=models.CASCADE,
        related_name='reacciones',
        null=True,
        blank=True,
        verbose_name="Noticia"
    )
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='reacciones',
        null=True,
        blank=True,
        verbose_name="Evento"
    )

    class Meta:
        db_table = 'reaccion'
        verbose_name = "Reacción"
        verbose_name_plural = "Reacciones"

    def __str__(self):
        destino = self.noticia if self.noticia else self.evento
        return f"{self.usuario} - {self.tipo} - {destino}"

    def clean(self):
        if self.noticia and self.evento:
            raise ValidationError("Una reacción no puede estar asociada a noticia y evento al mismo tiempo.")
        if not self.noticia and not self.evento:
            raise ValidationError("Una reacción debe estar asociada a una noticia o a un evento.")


class Mensaje(models.Model):
    emisor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='mensajes_enviados',
        verbose_name="Emisor"
    )
    receptor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='mensajes_recibidos',
        verbose_name="Receptor"
    )
    contenido = models.TextField(verbose_name="Contenido")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    class Meta:
        db_table = 'mensaje'
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['-fecha']

    def __str__(self):
        return f"Mensaje de {self.emisor} a {self.receptor}"


class Notificacion(models.Model):
    class TipoNotificacion(models.TextChoices):
        GLOBAL = 'GLOBAL', 'GLOBAL'
        COMUNEROS = 'COMUNEROS', 'COMUNEROS'
        PERSONAL = 'PERSONAL', 'PERSONAL'

    titulo = models.CharField(max_length=200, verbose_name="Título")
    mensaje = models.TextField(verbose_name="Mensaje")
    tipo = models.CharField(
        max_length=15,
        choices=TipoNotificacion.choices,
        verbose_name="Tipo"
    )
    usuario_destino = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='notificaciones',
        null=True,
        blank=True,
        verbose_name="Usuario destino"
    )
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    class Meta:
        db_table = 'notificacion'
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo

    def clean(self):
        if self.tipo == self.TipoNotificacion.PERSONAL and not self.usuario_destino:
            raise ValidationError("La notificación PERSONAL debe tener un usuario destino.")
        if self.tipo in [self.TipoNotificacion.GLOBAL, self.TipoNotificacion.COMUNEROS] and self.usuario_destino:
            raise ValidationError("Solo la notificación PERSONAL debe tener usuario destino.")


class Multimedia(models.Model):
    class TipoMultimedia(models.TextChoices):
        IMAGEN = 'IMAGEN', 'IMAGEN'
        VIDEO = 'VIDEO', 'VIDEO'

    url = models.CharField(max_length=255, verbose_name="URL o ruta")
    tipo = models.CharField(
        max_length=10,
        choices=TipoMultimedia.choices,
        verbose_name="Tipo"
    )
    noticia = models.ForeignKey(
        Noticia,
        on_delete=models.CASCADE,
        related_name='multimedia',
        null=True,
        blank=True,
        verbose_name="Noticia"
    )
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='multimedia',
        null=True,
        blank=True,
        verbose_name="Evento"
    )
    orden = models.IntegerField(verbose_name="Orden")
    fecha_subida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de subida")

    class Meta:
        db_table = 'multimedia'
        verbose_name = "Multimedia"
        verbose_name_plural = "Multimedia"
        ordering = ['orden', '-fecha_subida']

    def __str__(self):
        return self.url

    def clean(self):
        if self.noticia and self.evento:
            raise ValidationError("El archivo multimedia no puede estar asociado a noticia y evento al mismo tiempo.")
        if not self.noticia and not self.evento:
            raise ValidationError("El archivo multimedia debe estar asociado a una noticia o a un evento.")


class Reporte(models.Model):
    class TipoReporte(models.TextChoices):
        QUEJA = 'QUEJA', 'QUEJA'
        REPORTE_COMENTARIO = 'REPORTE_COMENTARIO', 'REPORTE_COMENTARIO'
        SUGERENCIA = 'SUGERENCIA', 'SUGERENCIA'

    class EstadoReporte(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'PENDIENTE'
        REVISADO = 'REVISADO', 'REVISADO'

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='reportes',
        verbose_name="Usuario"
    )
    tipo = models.CharField(
        max_length=25,
        choices=TipoReporte.choices,
        verbose_name="Tipo"
    )
    descripcion = models.TextField(verbose_name="Descripción")
    comentario = models.ForeignKey(
        Comentario,
        on_delete=models.CASCADE,
        related_name='reportes',
        null=True,
        blank=True,
        verbose_name="Comentario"
    )
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    estado = models.CharField(
        max_length=10,
        choices=EstadoReporte.choices,
        default=EstadoReporte.PENDIENTE,
        verbose_name="Estado"
    )

    class Meta:
        db_table = 'reporte'
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.tipo} - {self.usuario}"

    def clean(self):
        if self.tipo == self.TipoReporte.REPORTE_COMENTARIO and not self.comentario:
            raise ValidationError("Si el tipo es REPORTE_COMENTARIO, debes seleccionar un comentario.")