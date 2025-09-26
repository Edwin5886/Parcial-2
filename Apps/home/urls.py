from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('videos/', views.videos, name='videos'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('creditos/', views.creditos, name='creditos'),
]