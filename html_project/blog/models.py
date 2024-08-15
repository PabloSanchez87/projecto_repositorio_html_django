from django.db import models
from django.utils import timezone

# Modelo para un post de un blog.
class Post(models.Model):
    title = models.CharField(
        verbose_name='Título',
        max_length=200
        )
    
    content = models.TextField(
        verbose_name='Contenido',
        )
    
    author = models.CharField(
        verbose_name='Autor',
        max_length=100
        )
    
    created_at = models.DateTimeField(
        verbose_name='Fecha de creación',
        default=timezone.now
        ) # Cuando se ha creado esa entidad.
    
    show_home = models.BooleanField(
        verbose_name='Mostrar en home', 
        default=False
        )
    
    def __str__(self) -> str:
        return self.title