from django.db import models
from django.utils import timezone

# Modelo para un post de un blog.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now) # Cuando se ha creado esa entidad.