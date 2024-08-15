from django.contrib import admin
from .models import Post

# Damos de alta la entidad post en el admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('pk','title', 'author', 'created_at', 'show_home')  # Campos a mostrar en la lista
    list_display_links = ('title', 'author')  # Campos clicables para editar
    
    