from django.shortcuts import render

# Función modo ejemplo para enlazar con la un "home_view"
def home(request):
    return render(request, 'core/home.html')  # Render: Necesita un request y un template.
                                            # Busca el template en el archivo settings.py


def about_us(request):
    return render(request, 'core/about_us.html')


def login(request):
    return render(request, 'core/login.html')


def register(request):
    return render(request, 'core/register.html')

def contact(request):
    return render(request, 'core/contact.html')

