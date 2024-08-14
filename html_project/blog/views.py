from django.shortcuts import render

# Función modo ejemplo para enlazar con la un "home_view"
def blog_list(request):
    return render(request, 'blog/blog_list.html')  # Render: Necesita un request y un template.
                                            # Busca el template en el archivo settings.py


def blog_detail(request, id):
    return render(request, 'blog/blog_detail.html')


