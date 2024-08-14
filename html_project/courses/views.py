from django.shortcuts import render

# Función modo ejemplo para enlazar con la un "home_view"
def course_list(request):
    return render(request, 'courses/course_list.html')  # Render: Necesita un request y un template.
                                            # Busca el template en el archivo settings.py


def course_detail(request, id):
    return render(request, 'courses/course_detail.html')


