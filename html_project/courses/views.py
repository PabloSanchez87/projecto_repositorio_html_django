from django.shortcuts import render
from .models import Course  # Importa el modelo Course desde el archivo models.py.

# Create your views here.
# Vistas: Funciones que responden a las peticiones HTTP de los usuarios.
# Cada vista es una función que recibe un request y devuelve un response.
def course_list(request):
    all_courses = Course.objects.all()  # Obtiene todos los cursos de la base de datos.
    
    context = {'courses': all_courses}  # Crea un diccionario con los cursos para pasarlo al template.
    
    return render(request, 'courses/course_list.html', context)  # Render: Necesita un request y un template.
                                            # Busca el template en el archivo settings.py


def course_detail(request, id):
    course = Course.objects.get(pk=id)  # Obtiene un curso de la base de datos según su ID.
    context = {'course': course}  # Crea un diccionario con el curso para pasarlo al template.
    
    return render(request, 'courses/course_detail.html', context)


