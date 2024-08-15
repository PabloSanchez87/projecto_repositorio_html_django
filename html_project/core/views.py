from django.shortcuts import render
from courses.models import Course
from blog.models import Post

# Create your views here.
# Vistas: Funciones que responden a las peticiones HTTP de los usuarios.
# Cada vista es una función que recibe un request y devuelve un response.
def home(request):
    
    context = {
        'courses': Course.objects.filter(show_home=True),  # Filtra los cursos que se muestran en el home (show_home = True)
        'posts': Post.objects.filter(show_home=True),  # Filtra los posts que se muestran en el home (show_home = True)
    }
    
    return render(request, 'core/home.html', context)  # Render: Necesita un request y un template.
                                            # Busca el template en el archivo settings.py


def about_us(request):
    return render(request, 'core/about_us.html')


def login(request):
    return render(request, 'core/login.html')


def register(request):
    return render(request, 'core/register.html')

def contact(request):
    return render(request, 'core/contact.html')

