from django.shortcuts import render, redirect
from courses.models import Course
from blog.models import Post
from core.forms import ContactForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User



# Importamos send_mail para enviar correos electrónicos
from django.core.mail import send_mail

from .models import Contact


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



def logout_view(request):
    logout(request)  # Deslogeamos al usuario
    return redirect(reverse('core:home'))  # Redireccionamos a la página de login


# Vista para el registro
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Instanciamos el formulario con los datos enviados por POST
        if form.is_valid():  # Validamos que los datos enviados por el formulario sean válidos
            username = form.cleaned_data['username']  # Obtenemos el nombre de usuario del formulario
            first_name = form.cleaned_data['first_name']  # Obtenemos el primer nombre del formulario
            last_name = form.cleaned_data['last_name']  # Obtenemos el apellido del formulario
            email = form.cleaned_data['email']  # Obtenemos el email del formulario
            password1 = form.cleaned_data['password1']  # Obtenemos la contraseña del formulario

            # Creamos un nuevo usuario con los datos obtenidos del formulario
            user = User.objects.create_user(
                                            username=username, 
                                            email=email, 
                                            password=password1)  
            
            # Actualizamos los campos de nombre y apellido
            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.save()
            
            login(request, user)  # Logeamos al usuario     
                
            context = {
                'form': form,  # Pasamos el formulario al contexto
                'success_message': 'Usuario creado correctamente',  # Mensaje de éxito
                'success': True,  # Indicamos que se ha creado correctamente el usuario
            }    
            return render(request, 'core/home.html', context)  # Renderizamos la página de registro con el contexto
        
        else:
            context = {
                'form': form,  # Pasamos el formulario al contexto
                'error': True,  # Indicamos que hay un error en el formulario
                'error_message': 'Invalid username or password.',  # Mensaje de error si los datos no son válidos
            }
            return render(request, 'core/register.html', context)  # Renderizamos la plantilla con errores
    else:
        form = UserRegistrationForm()  # Instanciamos el formulario vacío
        context = {
            'form': form,  # Pasamos el formulario al contexto
            'error': False,  # Indicamos que no hay error en el formulario
        }
        return render(request, 'core/register.html', context)


# Vista para el contacto
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            nombre = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['message']
            
            Contact.objects.create(name=nombre, email=email, message=mensaje)
            
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

# # Vista para el login 
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():  # Si el formulario es válido
#             username = form.cleaned_data['username']  # Obtenemos el username del formulario
#             password = form.cleaned_data['password']  # Obtenemos la contraseña del formulario
            
#             user = authenticate(username=username, password=password)  # Autenticamos al usuario
#             if user is not None:  # Si el usuario existe
#                 login(request, user)  # Logeamos al usuario
                
#                 # Obtener el valor del parámetro 'next' si existe
#                 next_url = request.GET.get('next', None)
                
#                 # Si next_url está presente, redirigir allí, de lo contrario, redirigir a la página principal
#                 if next_url:
#                     return redirect(next_url)
#                 else:
#                     return redirect(reverse('core:home'))  # Redireccionamos a la página de inicio
        
#             else:
#                 context = {
#                     'form': form,  # Pasamos el formulario al contexto
#                     'error': True,  # Indicamos que hay un error en el formulario
#                     'error_message': 'Invalid username or password.',  # Mensaje de error si los datos no son válidos
#                 }
#                 return render(request, 'core/login.html', context)  # Renderizamos la página de login y pasamos el formulario al contexto
#         else:
#             context = {
#                 'form': form,  # Pasamos el formulario al contexto
#                 'error': True,  # Indicamos que hay un error en el formulario
#                 'error_message': 'Invalid username or password.',  # Mensaje de error si los datos no son válidos
#             }
#             return render(request, 'core/login.html', context)  # Renderizamos la página de login y pasamos el formulario al contexto
        
#     else:
#         form = LoginForm()  # Instanciamos el formulario vacío
#         context = {
#             'form': form,  # Pasamos el formulario al contexto
#         }
        
#         return render(request, 'core/login.html', context)
