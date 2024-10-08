# Generated by Django 5.1 on 2024-08-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_toc'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(blank=True, help_text='Ingrese la imagen del curso', null=True, upload_to='courses/images/', verbose_name='Imagen del curso'),
        ),
    ]
