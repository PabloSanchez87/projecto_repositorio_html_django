from django.urls import path

from .views import home, about_us, register, contact, logout_view

# importing the login view from django's built-in auth views module. This is a prebuilt function that allows users to log in.
from django.contrib.auth.views import LoginView


app_name="core"

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('contacto-con-nosotros/', contact, name='contact'),

    # this is a prebuilt function that allows users to log in. 
    # It takes the template name as an argument and returns a view that renders the login page. 
    # The name of the view is 'login'. This is used to link the login button on the homepage to the login page.
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'), 
    
    path('logout/', logout_view, name='logout'),
    
    path('register/', register, name='register'),
]