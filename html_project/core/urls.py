from django.urls import path

from .views import home, about_us, register, login, contact

app_name="core"

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('contacto-con-nosotros/', contact, name='contact'),
]