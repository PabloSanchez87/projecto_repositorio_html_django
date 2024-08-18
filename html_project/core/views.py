from django.shortcuts import render
from courses.models import Course
from blog.models import Post
from core.forms import ContactForm

# Importamos send_mail para enviar correos electrónicos
from django.core.mail import send_mail


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            nombre = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['message']
            
            # Aquí podrías guardar los datos en la base de datos o enviar un correo
            print(f'El usuario {nombre} con dirección {email} ha enviado el siguiente mensaje: {mensaje}')
            
            # Cambiaramos el print por la funcion send_mail de django.core.mail
            # Necesario configurar settings.py para que funcione send_mail
            # Mail is sent using the SMTP host and port specified in the EMAIL_HOST and EMAIL_PORT settings. 
            # The EMAIL_HOST_USER and EMAIL_HOST_PASSWORD settings, if set, are used to authenticate to the SMTP server, 
            # and the EMAIL_USE_TLS and EMAIL_USE_SSL settings control whether a secure connection is used.
            # Nota
            # The character set of email sent with django.core.mail will be set to the value of your DEFAULT_CHARSET setting.
            # send_mail(
            #     'Contacto desde el sitio web',  # Asunto del correo
            #     mensaje,  # Mensaje del correo
            #     'from@example.com',  # Remitente
            #     ['to@example.com'],  # Destinatario
            #     fail_silently=False  # Si falla el envio no detiene la ejecucion del codigo
            # )            
            
            context = {
                'form': form,
                'success': True,  # Indicamos que el formulario se envio correctamente
            }
            
            return render(request, 'core/contact.html', context)
        
    else:
        form = ContactForm()

    context = {
        'form': form
    }   
    
    return render(request, 'core/contact.html', context)

