
# Proyecto de Práctica con Django (En Construcción)

Este proyecto es un ejercicio práctico en el que se implementan diversas funcionalidades usando Django. El objetivo es explorar y aprender a manejar Django a través de la creación de una aplicación web que incluye un blog, cursos y un sistema de contacto.

## Características Principales

- **Blog**: Gestión de entradas de blog a través de Django Admin, con la posibilidad de mostrar entradas en la página principal.
- **Cursos**: Sistema para gestionar cursos, con la capacidad de subir imágenes y archivos relacionados, y mostrarlos en la página principal si se selecciona.
- **Formulario de Contacto**: Implementación de un formulario de contacto con almacenamiento en la base de datos y envío de correos electrónicos (pendiente de configuración del dominio).
- **Editor de Texto Avanzado**: Integración con CKEditor para mejorar la experiencia de edición de contenido.
- **Redimensionado de Imágenes**: Uso de thumbnails para redimensionar imágenes y optimizar su presentación.
- **Autenticación y Permisos**: Implementación de autenticación basada en sesiones y uso de decoradores para controlar el acceso a las vistas.
- **Base de Datos**: Utilización de SQLite para almacenamiento temporal y PostgreSQL en producción.

## Requisitos Previos

- Python 3.x
- Django
- CKEditor (para edición avanzada de texto)
- Thumbnails (para redimensionar imágenes)

## Instalación

1. Clona el repositorio:

2. Navega al directorio del proyecto:

3. Crea un entorno virtual:

   ```bash
   python -m venv venv
   ```

4. Activa el entorno virtual:

     ```bash
     source venv/bin/activate
     ```

5. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

6. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py migrate
   ```

7. Ejecuta el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

## Funcionalidades Implementadas

### Contactos

- Se guardan los contactos en la base de datos antes de enviarlos a través del formulario de contacto.
- El formulario de contacto permite la gestión de mensajes recibidos.

### Blog

- Gestión de publicaciones del blog desde el panel de administración de Django.
- Los artículos del blog se muestran en la página principal si están marcados para ser visibles.

### Cursos

- Los cursos se pueden añadir, editar y eliminar desde el panel de administración de Django.
- Cada curso puede incluir imágenes y archivos que se suben y gestionan desde la interfaz de administración.

### Configuración de Envío de Correos

- El envío de correos electrónicos está configurado pero actualmente deshabilitado debido a la necesidad de un dominio funcional.

### Redimensionado de Imágenes

- Se utiliza la librería Thumbnails para redimensionar y optimizar imágenes.

## Notas

- Asegúrate de configurar las credenciales de correo en `settings.py` para habilitar el envío de correos.
- Los archivos de medios subidos, como imágenes de cursos, se almacenan en la carpeta `media`.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork del repositorio y enviar tus pull requests. Cualquier sugerencia o mejora es bienvenida.


