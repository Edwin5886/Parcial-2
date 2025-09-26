from django.shortcuts import render

# Create your views here.

def home(request):
    """Vista principal del sitio"""
    return render(request, 'home.html')

def videos(request):
    """Vista de la página de videos de cursos"""
    # Lista de videos de ejemplo - puedes agregar más datos aquí
    videos_list = [
        {'titulo': 'Introducción a Python', 'duracion': '45 min', 'categoria': 'Programación'},
        {'titulo': 'HTML y CSS Básico', 'duracion': '60 min', 'categoria': 'Desarrollo Web'},
        {'titulo': 'JavaScript para Principiantes', 'duracion': '90 min', 'categoria': 'Desarrollo Web'},
        {'titulo': 'Base de Datos con MySQL', 'duracion': '75 min', 'categoria': 'Base de Datos'},
    ]
    context = {'videos': videos_list}
    return render(request, 'videos.html', context)

def usuarios(request):
    """Vista de la página de usuarios"""
    # Lista de usuarios de ejemplo
    usuarios_list = [
        {'nombre': 'María González', 'email': 'maria@email.com', 'cursos': 5},
        {'nombre': 'Carlos López', 'email': 'carlos@email.com', 'cursos': 3},
        {'nombre': 'Ana Rodríguez', 'email': 'ana@email.com', 'cursos': 7},
        {'nombre': 'Pedro Martín', 'email': 'pedro@email.com', 'cursos': 2},
    ]
    context = {'usuarios': usuarios_list}
    return render(request, 'usuarios.html', context)

def creditos(request):
    """Vista de la página de créditos"""
    return render(request, 'creditos.html')
