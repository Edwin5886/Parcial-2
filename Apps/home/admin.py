from django.contrib import admin
from .models import Usuario, Categoria, Curso, Video, Inscripcion, ProgresoVideo

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'fecha_registro', 'activo')
    list_filter = ('activo', 'fecha_registro')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')
    readonly_fields = ('fecha_registro',)
    fieldsets = (
        ('Usuario', {
            'fields': ('user', 'activo')
        }),
        ('Información Personal', {
            'fields': ('telefono', 'fecha_nacimiento', 'biografia')
        }),
        ('Fechas', {
            'fields': ('fecha_registro',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'color', 'activa', 'fecha_creacion')
    list_filter = ('activa', 'fecha_creacion')
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'instructor', 'nivel', 'precio', 'total_estudiantes', 'activo')
    list_filter = ('categoria', 'nivel', 'activo', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion', 'instructor__user__username')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion', 'total_estudiantes')
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'descripcion', 'categoria', 'instructor')
        }),
        ('Detalles del Curso', {
            'fields': ('nivel', 'precio', 'duracion_horas', 'activo')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'orden', 'duracion_minutos', 'activo')
    list_filter = ('curso', 'activo', 'fecha_subida')
    search_fields = ('titulo', 'curso__titulo')
    readonly_fields = ('fecha_subida',)
    fieldsets = (
        ('Información del Video', {
            'fields': ('titulo', 'descripcion', 'curso', 'url_video')
        }),
        ('Configuración', {
            'fields': ('orden', 'duracion_minutos', 'activo')
        }),
        ('Fechas', {
            'fields': ('fecha_subida',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso', 'progreso', 'completado', 'calificacion', 'fecha_inscripcion')
    list_filter = ('completado', 'activa', 'calificacion', 'fecha_inscripcion')
    search_fields = ('usuario__user__username', 'curso__titulo')
    readonly_fields = ('fecha_inscripcion', 'fecha_completado')
    fieldsets = (
        ('Inscripción', {
            'fields': ('usuario', 'curso', 'activa')
        }),
        ('Progreso', {
            'fields': ('progreso', 'completado', 'fecha_completado')
        }),
        ('Evaluación', {
            'fields': ('calificacion', 'comentario')
        }),
        ('Fechas', {
            'fields': ('fecha_inscripcion',),
            'classes': ('collapse',)
        }),
    )


@admin.register(ProgresoVideo)
class ProgresoVideoAdmin(admin.ModelAdmin):
    list_display = ('inscripcion', 'video', 'visto', 'minutos_vistos', 'fecha_visto')
    list_filter = ('visto', 'fecha_visto')
    search_fields = ('inscripcion__usuario__user__username', 'video__titulo')
    readonly_fields = ('fecha_visto',)
