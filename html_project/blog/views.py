from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_list(request):
    all_posts = Post.objects.all()  # Obtiene todos los posts de la base de datos.
    
    context  = {'posts': all_posts}   # Crea un diccionario con los datos que se pasan al template.
    
    return render(request, 'blog/blog_list.html', context)  # Render: Necesita un request y un template.
                                            # Busca el template en el archivo settings.py


def blog_detail(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'post': post
        }
    return render(request, 'blog/blog_detail.html', context)


 