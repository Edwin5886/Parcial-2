from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    """Modelo para gestionar usuarios de la plataforma"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    biografia = models.TextField(max_length=500, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Categoria(models.Model):
    """Modelo para categorías de cursos"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=300, blank=True, null=True)
    color = models.CharField(max_length=7, default='#007bff', help_text='Color en formato hexadecimal')
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class Curso(models.Model):
    """Modelo para cursos en línea"""
    NIVELES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='cursos')
    instructor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cursos_impartidos')
    nivel = models.CharField(max_length=20, choices=NIVELES, default='principiante')
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    duracion_horas = models.PositiveIntegerField(help_text='Duración en horas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
    @property
    def total_estudiantes(self):
        return self.inscripciones.filter(activa=True).count()
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-fecha_creacion']


class Video(models.Model):
    """Modelo para videos de los cursos"""
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='videos')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    url_video = models.URLField(help_text='URL del video (YouTube, Vimeo, etc.)')
    duracion_minutos = models.PositiveIntegerField(help_text='Duración en minutos')
    orden = models.PositiveIntegerField(default=1, help_text='Orden del video en el curso')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.curso.titulo} - {self.titulo}"
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['curso', 'orden']
        unique_together = ['curso', 'orden']


class Inscripcion(models.Model):
    """Modelo para inscripciones de usuarios a cursos"""
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    progreso = models.PositiveIntegerField(default=0, help_text='Progreso en porcentaje (0-100)')
    completado = models.BooleanField(default=False)
    fecha_completado = models.DateTimeField(blank=True, null=True)
    calificacion = models.PositiveIntegerField(blank=True, null=True, choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField(blank=True, null=True)
    activa = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.usuario.user.username} - {self.curso.titulo}"
    
    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        unique_together = ['usuario', 'curso']


class ProgresoVideo(models.Model):
    """Modelo para el progreso de videos por usuario"""
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, related_name='progreso_videos')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    visto = models.BooleanField(default=False)
    fecha_visto = models.DateTimeField(blank=True, null=True)
    minutos_vistos = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.inscripcion.usuario.user.username} - {self.video.titulo}"
    
    class Meta:
        verbose_name = "Progreso de Video"
        verbose_name_plural = "Progreso de Videos"
        unique_together = ['inscripcion', 'video']
