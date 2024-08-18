# Generated by Django 5.1 on 2024-08-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Correo Electronico')),
                ('message', models.TextField(max_length=5000, verbose_name='Mensaje')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]