from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

# Create your forms here.
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
    
    
# Formulario de inicio de sesión
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label="Nombre de usuario")
    first_name = forms.CharField(max_length=100, label="Nombre")
    last_name = forms.CharField(max_length=100, label="Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repite Password")

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        validate_password(password2)
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email