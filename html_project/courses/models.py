from django.db import models

class Course(models.Model):
    tittle = models.CharField(
        verbose_name='Título del curso',
        help_text='Ingrese el título del curso',
        max_length=200)
    
    content = models.TextField(
        verbose_name='Descripción',
        help_text='Ingrese una descripción del curso',
    )
    
    call_link = models.URLField(
        verbose_name='Enlace de llamada',
        help_text='Ingrese el enlace de llamada del curso',
        blank=True,
        null=True,
    )
    
    created_at = models.DateTimeField(
        verbose_name='Fecha de creación',
        help_text='Ingrese la fecha de creación del curso',
        blank=True,
        null=True,
        auto_now_add=True)
    
    # Check_box para indicar si se muestra en la home.
    show_home = models.BooleanField(
        verbose_name='Mostrar en home', 
        default=False
        )
    
    # Archivo PDF con la tabla de contenidos del curso. 
    # Solo se puede subir un archivo por curso. Si se sube otro, el anterior se borra.
    toc = models.FileField(
        verbose_name='Tabla de contenidos',
        help_text='Ingrese el archivo PDF con la tabla de contenidos del curso',
        upload_to='courses/tocs/',
        blank=True,
        null=True,
    )
    
    # Imagen del curso. Solo se puede subir una imagen por curso. 
    # Si se sube otra, la anterior se borra.
    course_image = models.ImageField(
        verbose_name='Imagen del curso',
        help_text='Ingrese la imagen del curso',
        upload_to='courses/images/',
        blank=True,
        null=True,
    )
    
    def __str__(self) -> str:
        return self.tittle
