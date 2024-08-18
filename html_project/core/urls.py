from django.urls import path

from .views import home, about_us, register, login_view, contact, logout_view

app_name="core"

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contacto-con-nosotros/', contact, name='contact'),
]