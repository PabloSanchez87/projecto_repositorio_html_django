# Generated by Django 5.1 on 2024-08-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='show_home',
            field=models.BooleanField(default=False, verbose_name='Mostrar en home'),
        ),
    ]