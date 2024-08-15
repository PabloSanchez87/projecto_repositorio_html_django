from django.contrib import admin
from .models import Post

# Damos de alta la entidad post en el admin
admin.site.register(Post)