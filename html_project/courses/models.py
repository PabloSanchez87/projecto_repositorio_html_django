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
    
    show_home = models.BooleanField(
        verbose_name='Mostrar en home', 
        default=False
        )
    
    toc = models.FileField(
        verbose_name='Tabla de contenidos',
        help_text='Ingrese el archivo PDF con la tabla de contenidos del curso',
        upload_to='courses/tocs/%Y/%m/%d',
        blank=True,
        null=True,
    )
    
    def __str__(self) -> str:
        return self.tittle
