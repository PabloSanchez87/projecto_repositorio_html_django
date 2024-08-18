from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=200)
    email = models.EmailField(verbose_name='Correo Electronico',
                              max_length=255, 
                              unique=True, 
                              db_index=True, 
                              blank=False, 
                              null=False)
    message = models.TextField(verbose_name='Mensaje', max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name