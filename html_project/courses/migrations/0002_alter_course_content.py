# Generated by Django 5.1 on 2024-08-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='content',
            field=models.TextField(help_text='Ingrese una descripción del curso', verbose_name='Descripción'),
        ),
    ]
